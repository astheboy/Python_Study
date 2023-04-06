# 필요한 라이브러리를 import 합니다.

import os  # os 모듈을 import
import sys
import webbrowser  # webbrowser 모듈을 import
import pyvibe as pv

# PyVibe 모듈을 사용하여 웹페이지를 만듭니다.
page = pv.Page()
page.add_header("Welcome to PyVibe!")
page.add_text(
    "PyVibe 라이브러리를 이용한 파이썬으로 웹페이지 만들기.")
page.add_card("카드 메뉴")
page.add_image(
    "https://th.bing.com/th/id/OIG.hSoAkYUAa9FvVGopGuST?pid=ImgGn", "Bing 생성 이미지 테스트")


# 출력할 내용을 변수에 저장합니다.


# Generate the HTML code
html_code = page.to_html()

# Get the path of the current directory
current_directory = os.getcwd()

# Define the file path for saving the HTML file
file_path = os.path.join(current_directory, "main.html")

# Write the HTML code to the file
with open(file_path, "w") as f:
    f.write(html_code)

# Open the HTML file in Microsoft Edge on all platforms
edge_path = None
if sys.platform == "win32":
    # Windows
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
elif sys.platform == "darwin":
    # macOS
    edge_path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
elif sys.platform.startswith("linux"):
    # Linux
    edge_path = "/usr/bin/microsoft-edge"

if edge_path is not None:
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open('file://' + file_path)
else:
    print("이 웹페이지는 마이크로소프트 엣지 브라우저에 최적화 되어 있습니다. 엣지 브라우저를 설치해 주세요. ")
