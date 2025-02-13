from config import PROVIDERS, TEST_MESSAGES
from providers import test_provider

def main():
    results = []
    for provider in PROVIDERS:
        result = test_provider(provider, TEST_MESSAGES)
        if result:
            results.append(result)

    # 可以在这里添加结果的汇总分析
    if results:
        print("\n所有服务商测试结果汇总：")
        for result in results:
            print(f"\n{result['provider']}:")
            print(f"首token响应时间: {result['first_token_time']:.2f}s")
            print(f"总生成速度: {result['overall_tokens'] / result['total_time']:.2f} tokens/s")

if __name__ == "__main__":
    main()