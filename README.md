# DWCIC-Bot

Discord 學生年級身份組自動更新機器人

## Docker 部署
1. 建立 `.env` 檔案並設定 Discord Token：
   ```
   TOKEN=你的Discord機器人Token
   ```

2. 使用 Docker Compose 建立並啟動容器：
   ```bash
   docker-compose up -d
   ```

3. 檢視日誌：
   ```bash
   docker-compose logs -f
   ```

4. 停止機器人：
   ```bash
   docker-compose down
   ```

## 一般安裝步驟
1. 安裝 Python 3.8 或更新版本
2. 安裝相依套件：`pip install -r requirements.txt`
3. 建立 `.env` 檔案並設定 Discord 機器人 token：
   ```
   TOKEN=你的機器人token
   ```
4. 執行機器人：`python bot.py`

## 注意事項
- 確保伺服器中已建立「高一」、「高二」、「高三」、「已畢業」四個身份組
- 機器人需要管理身份組的權限
