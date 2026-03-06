@echo off
REM ------------------------------
REM 一键上传 PDE 项目到 GitHub
REM ------------------------------

REM 设置 Git 用户信息
git config --global user.name "zhongsude"
git config --global user.email "zhongsude6@gmail.com"

REM 初始化 Git 仓库（如果已存在可忽略）
git init

REM 添加远程仓库（如果已存在，可删除 origin 再添加）
git remote remove origin 2>nul
git remote add origin https://github.com/zhongsude/PDE.git

REM 添加所有文件
git add .

REM 提交更改
git commit -m "Add full PDE project"

REM 设置主分支为 main
git branch -M main

REM 推送到 GitHub
git push -u origin main

echo.
echo ✅ PDE 项目已成功上传到 GitHub！
pause