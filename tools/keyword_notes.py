from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class KeywordNote:
    """Represents a single keyword note with metadata."""
    keyword: str
    source_url: str
    note: str
    created_at: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formatted(self) -> str:
        """Return a human-readable representation of the note."""
        tag_part = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词：{self.keyword}\n"
            f"来源网址：{self.source_url}\n"
            f"创建时间：{self.created_at}\n"
            f"标签：{tag_part}\n"
            f"笔记内容：{self.note}\n"
        )


@dataclass
class KeywordNoteCollection:
    """A collection of keyword notes with utility methods."""
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if n.keyword == keyword]

    def all_formatted(self) -> str:
        """Return all notes formatted as a single text block."""
        lines = []
        for i, note in enumerate(self.notes, 1):
            lines.append(f"--- 笔记 {i} ---")
            lines.append(note.formatted())
        return "\n".join(lines)

    def count(self) -> int:
        return len(self.notes)


def create_sample_notes() -> KeywordNoteCollection:
    """Create a set of pre-defined sample notes for demonstration."""
    collection = KeywordNoteCollection()

    note1 = KeywordNote(
        keyword="中彩网",
        source_url="https://ssl-cn-zhcw.com",
        note="中彩网是中国福利彩票的官方网站，提供各类彩票资讯与数据。",
        tags=["彩票", "福利彩票", "官网"]
    )

    note2 = KeywordNote(
        keyword="中彩网",
        source_url="https://ssl-cn-zhcw.com/kjxx",
        note="中彩网开奖信息页面，可以查询最新开奖号码。",
        tags=["开奖信息", "查询"]
    )

    note3 = KeywordNote(
        keyword="双色球",
        source_url="https://ssl-cn-zhcw.com/ssq",
        note="双色球是福利彩票中最受欢迎的游戏之一。",
        tags=["双色球", "彩票游戏"]
    )

    collection.add_note(note1)
    collection.add_note(note2)
    collection.add_note(note3)

    return collection


def filter_by_tag(collection: KeywordNoteCollection, tag: str) -> List[KeywordNote]:
    """Return notes that contain a specific tag."""
    return [note for note in collection.notes if tag in note.tags]


def export_to_text(collection: KeywordNoteCollection, filepath: str) -> None:
    """Write formatted notes to a text file."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(collection.all_formatted())


def main() -> None:
    """Demonstrate usage of KeywordNote and KeywordNoteCollection."""
    notes = create_sample_notes()
    print("所有笔记：")
    print(notes.all_formatted())

    print("按关键词 '中彩网' 筛选：")
    for note in notes.find_by_keyword("中彩网"):
        print(note.formatted())

    print("按标签 '彩票游戏' 筛选：")
    for note in filter_by_tag(notes, "彩票游戏"):
        print(note.formatted())

    print(f"笔记总数：{notes.count()}")


if __name__ == "__main__":
    main()