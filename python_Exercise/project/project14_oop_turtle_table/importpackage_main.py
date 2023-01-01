#prettytabel package - https://pypi.org/project/prettytable/

from prettytable import PrettyTable, MSWORD_FRIENDLY, MARKDOWN
from prettytable.colortable import ColorTable, Themes

table = PrettyTable()

table.field_names = ["도시이름", "도시 번호", "인구수", "강수량"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
table.align = "r"
table.sortby = "강수량"
table.set_style(MSWORD_FRIENDLY)
print("\n")
print(table)

table.set_style(MARKDOWN)
print("\n")
print(table)

# 색 테이블로 변경
colortable = ColorTable(theme=Themes.OCEAN)

colortable.field_names = ["도시이름", "도시 번호", "인구수", "강수량"]
colortable.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
colortable.align = "r"
colortable.sortby = "강수량"

colortable.set_style(MARKDOWN)
print("\n")
print(colortable)