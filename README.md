# 课程组队信息

通用人工智能创新实践课的组队登记仓库：各队以 PR 向 [teams.md](teams.md) 追加一行，即第 2 讲的作业。

- 仓库地址：GitHub【待定】 · Gitee【待定】，任选其一
- 截止：第 6 周结束前

## 前提

- 已在 GitHub 或 Gitee 的账号设置中添加 SSH 公钥
- 已组队，3–5 人

## 提交流程

学生对本仓库无写权限，改动经本人的 fork 提交。

1. 打开本仓库的网页，点击右上角的 **Fork** 按钮，在本人账号下创建一份副本，即本人的 fork
2. 在本人 fork 的网页上点击 **Code**（Gitee 为「克隆/下载」），复制 SSH 地址；clone 到本地并新建分支

   ```bash
   git clone git@<平台>.com:<you>/<repo>.git   # <平台> 为 github 或 gitee
   cd <repo>
   git switch -c add-team
   ```

3. 在 teams.md 表格末尾追加本队一行，每位成员占一列，填真实姓名，空余的列留空；检查格式后提交，push 到本人的 fork

   ```markdown
   |示例队|张三|李四|王五|||
   ```

   ```bash
   python scripts/check_teams.py
   git add teams.md
   git commit -m "docs: add team <队名>"
   git push -u origin HEAD
   ```

4. 回到本人 fork 的网页，点击 **Pull request**（GitHub 在 push 后会出现 **Compare & pull request** 按钮），目标选本仓库的 `main`，标题同提交信息，提交 PR。助教在 PR 页面 review 后合并；被要求修改时在本地修改、提交并 push 到同一分支，PR 自动更新
5. 若 PR 页面提示冲突（先合并的 PR 也追加在文件末尾），将本仓库最新的 `main` 合入本人的分支，两边的行都保留：

   ```bash
   git remote add upstream <本仓库地址>
   git fetch upstream
   git merge upstream/main
   # 编辑 teams.md：删除冲突标记，两边的行都保留
   git add teams.md && git commit
   git push
   ```

每队只提一个 PR，改动只有 teams.md 的一行；只填姓名，不填学号等其他个人信息。
