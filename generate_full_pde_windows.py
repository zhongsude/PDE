import os
from textwrap import dedent

# 1️⃣ 创建目录结构
folders = [
    "backend/services",
    "collectors",
    "analysis",
    "database",
    "frontend/dashboard/pages",
    "scripts",
    "docker/logs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# 2️⃣ 文件内容
files = {
    # 后端 FastAPI
    "backend/main.py": dedent('''
        from fastapi import FastAPI
        app = FastAPI()

        @app.get("/projects/top")
        def get_top_projects():
            return {"message": "Top projects placeholder"}
    '''),

    "backend/services/opportunity_engine.py": dedent('''
        # 机会评分计算逻辑
        def calculate_opportunity(trend_score, demand_score, competition_score, difficulty_score):
            return trend_score + demand_score - competition_score - difficulty_score
    '''),

    # 数据库
    "database/models.py": dedent('''
        from sqlalchemy import Column, String, Float, Boolean, DateTime
        from sqlalchemy.ext.declarative import declarative_base

        Base = declarative_base()

        class Trend(Base):
            __tablename__ = "trend"
            id = Column(String, primary_key=True)
            keyword = Column(String)
            source = Column(String)
            growth_rate = Column(Float)
            volume = Column(Float)
            timestamp = Column(DateTime)

        class Opportunity(Base):
            __tablename__ = "opportunity"
            id = Column(String, primary_key=True)
            project_name = Column(String)
            opportunity_score = Column(Float)
            trend_score = Column(Float)
            demand_score = Column(Float)
            competition_score = Column(Float)
            difficulty_score = Column(Float)
            is_blue_ocean = Column(Boolean)
            timestamp = Column(DateTime)
    '''),

    # Collectors 模板
    "collectors/base_collector.py": dedent('''
        class BaseCollector:
            def fetch(self): pass
            def parse(self, data): pass
            def save(self, data): pass
    '''),

    "collectors/google_trends.py": dedent('''
        from .base_collector import BaseCollector
        class GoogleTrendsCollector(BaseCollector):
            def fetch(self):
                return [{"keyword":"solar night light","growth_rate":85,"volume":12000}]
            def parse(self, data): return data
            def save(self, data): pass
    '''),

    "collectors/reddit_collector.py": dedent('''
        from .base_collector import BaseCollector
        class RedditCollector(BaseCollector):
            def fetch(self):
                return [{"keyword":"solar night lamp","growth_rate":70,"volume":5000}]
            def parse(self, data): return data
            def save(self, data): pass
    '''),

    "collectors/tiktok_collector.py": dedent('''
        from .base_collector import BaseCollector
        class TikTokCollector(BaseCollector):
            def fetch(self):
                return [{"keyword":"solar night lamp","growth_rate":75,"volume":10000}]
            def parse(self, data): return data
            def save(self, data): pass
    '''),

    "collectors/amazon_collector.py": dedent('''
        from .base_collector import BaseCollector
        class AmazonCollector(BaseCollector):
            def fetch(self):
                return [{"keyword":"solar night lamp","growth_rate":60,"volume":5000}]
            def parse(self, data): return data
            def save(self, data): pass
    '''),

    "collectors/producthunt_collector.py": dedent('''
        from .base_collector import BaseCollector
        class ProductHuntCollector(BaseCollector):
            def fetch(self):
                return [{"keyword":"solar night lamp","growth_rate":50,"volume":3000}]
            def parse(self, data): return data
            def save(self, data): pass
    '''),

    # Analysis
    "analysis/run_analysis.py": dedent('''
        print("Running analysis...")
        # NLP + 趋势预测 + 机会评分逻辑可在这里实现
    '''),

    "analysis/generate_report.py": dedent('''
        print("Generating PDF report...")
        # 每日报告生成逻辑
    '''),

    # 调度脚本
    "scripts/run_daily.sh": dedent('''
        #!/bin/bash
        echo "Starting PDE daily tasks..."
        python backend/main.py
        python analysis/run_analysis.py
        python analysis/generate_report.py
    '''),

    # Docker 文件
    "docker/Dockerfile.backend": dedent('''
        FROM python:3.11-slim
        WORKDIR /app
        COPY ../requirements.txt .
        RUN pip install --no-cache-dir -r requirements.txt
        COPY ../backend ./backend
        COPY ../collectors ./collectors
        COPY ../analysis ./analysis
        COPY ../database ./database
        COPY ../scripts ./scripts
        EXPOSE 8000
        CMD ["python", "backend/main.py"]
    '''),

    "docker/Dockerfile.frontend": dedent('''
        FROM node:20-alpine
        WORKDIR /app
        COPY ../frontend/dashboard/package.json .
        COPY ../frontend/dashboard/package-lock.json .
        RUN npm install
        COPY ../frontend/dashboard .
        EXPOSE 3000
        CMD ["npm", "run", "dev"]
    '''),

    "docker/docker-compose.yml": dedent('''
        version: "3.9"
        services:
          postgres:
            image: postgres:15
            environment:
              POSTGRES_USER: user
              POSTGRES_PASSWORD: password
              POSTGRES_DB: pde
            ports:
              - "5432:5432"
          backend:
            build:
              context: .
              dockerfile: Dockerfile.backend
            ports:
              - "8000:8000"
            depends_on:
              - postgres
          frontend:
            build:
              context: .
              dockerfile: Dockerfile.frontend
            ports:
              - "3000:3000"
            depends_on:
              - backend
    '''),

    # 占位 README
    "README.md": dedent('''
        # PDE Project
        完整 PDE 系统，包括：
        - 多来源爬虫（Google Trends, TikTok, Reddit, Amazon, Product Hunt）
        - NLP + 趋势分析 + 机会评分
        - FastAPI 后端 + React Dashboard
        - Docker 一键部署
        - 每日自动化调度
    ''')
}

# 3️⃣ 创建文件（Windows 安全: 根目录文件不报错, utf-8 编码）
for path, content in files.items():
    dir_name = os.path.dirname(path)
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("✅ PDE 完整项目文件已生成完成（Windows 安全 UTF-8）")