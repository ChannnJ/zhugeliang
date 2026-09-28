"""检查 teams.md 的格式。仅用标准库，运行方式：python scripts/check_teams.py"""

import sys
from pathlib import Path

TEAMS = Path(__file__).resolve().parent.parent / "teams.md"
HEADER = "|队名|成员1|成员2|成员3|成员4|成员5|"
MIN_MEMBERS, MAX_MEMBERS = 3, 5


def split_row(line: str) -> list[str] | None:
    line = line.strip()
    if not (line.startswith("|") and line.endswith("|")):
        return None
    return [cell.strip() for cell in line[1:-1].split("|")]


def check(text: str) -> list[str]:
    errors = []
    lines = text.splitlines()

    for no, line in enumerate(lines, 1):
        if line.startswith(("<<<<<<<", "=======", ">>>>>>>")):
            errors.append(f"第 {no} 行：残留冲突标记 {line[:7]}")

    try:
        start = [line.replace(" ", "") for line in lines].index(HEADER)
    except ValueError:
        return errors + [f"未找到表头 {HEADER}"]
    if start + 1 >= len(lines) or split_row(lines[start + 1]) is None:
        return errors + ["表头下一行应为分隔行 |---|---|---|---|---|---|"]

    teams: dict[str, int] = {}
    members: dict[str, tuple[int, str]] = {}
    for no, line in enumerate(lines[start + 2 :], start + 3):
        if not line.strip():
            continue
        cells = split_row(line)
        if cells is None:
            errors.append(f"第 {no} 行：表格之后不应有其他内容，或该行缺少首尾的 |")
            continue
        if len(cells) != 6:
            errors.append(
                f"第 {no} 行：应为 6 列（队名 + 5 个成员列），实际 {len(cells)} 列"
            )
            continue

        team, names = cells[0], cells[1:]
        if not team:
            errors.append(f"第 {no} 行：队名为空")
        elif team in teams:
            errors.append(f"第 {no} 行：队名「{team}」与第 {teams[team]} 行重复")
        else:
            teams[team] = no

        filled = [n for n in names if n]
        if not MIN_MEMBERS <= len(filled) <= MAX_MEMBERS:
            errors.append(
                f"第 {no} 行：成员 {len(filled)} 人，应为 {MIN_MEMBERS}–{MAX_MEMBERS} 人"
            )
        if names[: len(filled)] != filled:
            errors.append(f"第 {no} 行：成员应从「成员1」起连续填写，空余的列留在末尾")
        for name in filled:
            if name in members:
                prev_no, prev_team = members[name]
                errors.append(
                    f"第 {no} 行：成员「{name}」已出现在第 {prev_no} 行的「{prev_team}」"
                )
            else:
                members[name] = (no, team)

    return errors


def main() -> int:
    errors = check(TEAMS.read_text(encoding="utf-8"))
    for e in errors:
        print(f"teams.md {e}")
    if not errors:
        print("teams.md 格式检查通过")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
