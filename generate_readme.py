import os

PLATFORMS = {
    "boj": "https://www.acmicpc.net/problem/",
    "leetcode": "https://leetcode.com/problems/",
    "prog": "https://school.programmers.co.kr/",
    "codeforces": "https://codeforces.com/problemset/problem/",
    "atcoder": "https://atcoder.jp/contests/"
}

def get_problem_link(platform, filename):
    if platform == "boj":
        number = filename.split('.')[0]
        return PLATFORMS["boj"] + number
    elif platform == "leetcode":
        # expects: 1_two_sum.cpp
        slug = filename.split('.', 1)[0].split('_', 1)[1].replace('_', '-')
        return PLATFORMS["leetcode"] + slug
    else:
        return ""

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(base_dir, "README.md")

    lines = ["# 📘 알고리즘 문제 풀이 목록\n", "| 플랫폼 | 분류 | 문제 | 링크 |", "|---------|--------|--------|--------|"]

    for platform in os.listdir(base_dir):
        platform_path = os.path.join(base_dir, platform)
        if not os.path.isdir(platform_path) or platform == ".vscode":
            continue

        for category in os.listdir(platform_path):
            category_path = os.path.join(platform_path, category)
            if not os.path.isdir(category_path):
                continue

            for file in os.listdir(category_path):
                if file.endswith(".cpp"):
                    title = file.split('.')[0]
                    link = get_problem_link(platform, file)
                    lines.append(f"| {platform} | {category} | {title} | [문제링크]({link}) |")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("✅ README.md 생성 완료!")

if __name__ == "__main__":
    main()
