# DeepSeek 模型测试工具

这是一个用于测试不同服务商提供的 DeepSeek 模型性能的工具。它可以帮助您评估各个服务商的响应时间、生成速度等关键指标，从而选择最适合您需求的服务提供商。

## 功能特点

- 支持多个服务商的 DeepSeek 模型测试
- 实时流式输出生成内容
- 统计详细的性能指标，包括：
  - 首个 token 的响应时间
  - Reasoning 阶段的生成速度
  - Content 阶段的生成速度
  - 总体生成速度和时间
- 自动汇总多个服务商的测试结果

## 支持的服务商

- 火山引擎
- DeepSeek 官方
- 阿里云/百炼
- 腾讯云
- PPInfra
- Nvidia NIM
- （你可以自行添加）

## 服务商性能对比

| 服务商 | 首token响应时间 | 总生成速度 | 免费计划 |
|--------|----------------|------------|----------|
| 火山引擎 | 0.89s | 24.91 tokens/s | 50万免费Tokens |
| 阿里云/百炼 | 1.71s | 3.18 tokens/s | 新用户免费额度，可申请 |
| 腾讯云 | 1.95s | 10.04 tokens/s | 免费使用到2025年2月25日 |
| PPInfra | 1.39s | 10.83 tokens/s | 使用[邀请链接](https://ppinfra.com/user/register?invited_by=ZQRQZZ)获得300万R1 Tokens |
| Nvidia NIM | 57.60s | 2.75 tokens/s | 有一定免费额度 |

## 环境要求

- Python 3.x
- 必要的 Python 包（在 requirements.txt 中列出）：
  - openai==1.3.7
  - python-dotenv==1.0.0
  - pytz==2023.3.post1

## 安装步骤

1. 克隆或下载本项目到本地

2. 安装依赖包：
   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量：
   - 复制 `.env.example`（如果存在）或创建新的 `.env` 文件
   - 在 `.env` 文件中设置各个服务商的 API 密钥：
     ```
     DEEPSEEK_API_KEY="your-deepseek-api-key"
     ALIBABA_API_KEY="your-alibaba-api-key"
     TENCENT_API_KEY="your-tencent-api-key"
     PPINFRA_API_KEY="your-ppinfra-api-key"
     NVIDIA_API_KEY="your-nvidia-api-key"
     ```

## 使用方法

1. 配置测试参数：
   - 在 `config.py` 中可以修改 `TEST_MESSAGES` 来设置测试用的提示语
   - 可以根据需要在 `PROVIDERS` 列表中添加或删除要测试的服务商

2. 运行测试：
   ```bash
   python main.py
   ```

3. 查看结果：
   - 程序会实时显示每个服务商的生成内容
   - 每个服务商测试完成后会显示详细的性能指标
   - 最后会显示所有服务商的测试结果汇总

## 测试结果说明

测试结果包含以下关键指标：

- **首 token 响应时间**：从发送请求到收到第一个 token 的时间，反映服务的初始响应速度
- **Reasoning 部分**：模型思考阶段的 token 数量、用时和生成速度
- **Content 部分**：模型输出内容的 token 数量、用时和生成速度
- **总体生成**：整个过程的总 token 数量、总用时和平均生成速度

## 注意事项

- 请确保您有相应服务商的有效 API 密钥
- 测试结果可能会因网络状况、服务器负载等因素而波动
- 建议多次运行测试以获得更准确的性能评估

## 问题反馈

如果您在使用过程中遇到任何问题，或有改进建议，欢迎提出 Issue 或贡献代码。