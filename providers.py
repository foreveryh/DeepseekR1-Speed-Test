import time
from openai import OpenAI

def count_tokens(text):
    return len(text.split())

def test_provider(provider_config, messages):
    """
    根据传入的 provider 配置及消息，测试生成过程，并统计各阶段指标。
    如果测试过程中出现任何错误，则打印错误信息并跳过当前服务商。
    """
    provider_name = provider_config.get("name", "Unnamed Provider")
    print(f"\n---------------------------")
    print(f"开始测试服务商：{provider_name}")
    print(f"---------------------------\n")

    try:
        api_key = provider_config.get("api_key")
        base_url = provider_config.get("base_url")
        model = provider_config.get("model")

        client = OpenAI(api_key=api_key, base_url=base_url)

        reasoning_tokens = 0
        content_tokens = 0
        overall_tokens = 0

        reasoning_text = ""
        content_text = ""

        start_time = time.time()
        first_token_time = None

        reasoning_start_time = None
        reasoning_end_time = None
        content_start_time = None
        content_end_time = None

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True
        )

        for chunk in response:
            if not chunk.choices:
                if chunk.usage:
                    print("\n\n【Usage 信息】")
                    print(chunk.usage)
                continue

            delta = chunk.choices[0].delta
            reasoning_piece = getattr(delta, 'reasoning_content', "")
            content_piece = getattr(delta, 'content', "")

            if first_token_time is None and (reasoning_piece or content_piece):
                first_token_time = time.time() - start_time

            if reasoning_piece:
                if reasoning_start_time is None:
                    reasoning_start_time = time.time()
                reasoning_text += reasoning_piece
                tokens = count_tokens(reasoning_piece)
                reasoning_tokens += tokens
                overall_tokens += tokens
                reasoning_end_time = time.time()
                print(reasoning_piece, end='', flush=True)

            elif content_piece:
                if content_start_time is None:
                    content_start_time = time.time()
                content_text += content_piece
                tokens = count_tokens(content_piece)
                content_tokens += tokens
                overall_tokens += tokens
                content_end_time = time.time()
                print(content_piece, end='', flush=True)

        total_time = time.time() - start_time
        reasoning_time = (reasoning_end_time - reasoning_start_time) if (reasoning_start_time and reasoning_end_time) else 0
        content_time = (content_end_time - content_start_time) if (content_start_time and content_end_time) else 0

        print("\n\n【%s】" % provider_name)
        if first_token_time is not None:
            print(f"首 token 响应时间：{first_token_time:.2f} 秒")
        else:
            print("未收到 token 响应。")

        print(f"Reasoning 部分：{reasoning_tokens} tokens, 用时：{reasoning_time:.2f} 秒, 生成速度：{reasoning_tokens / reasoning_time if reasoning_time > 0 else 0:.2f} tokens/s")
        print(f"Content 部分：{content_tokens} tokens, 用时：{content_time:.2f} 秒, 生成速度：{content_tokens / content_time if content_time > 0 else 0:.2f} tokens/s")
        print(f"总体生成：{overall_tokens} tokens, 总用时：{total_time:.2f} 秒, 生成速度：{overall_tokens / total_time if total_time > 0 else 0:.2f} tokens/s")
        print("\n---------------------------\n")

        return {
            "provider": provider_name,
            "first_token_time": first_token_time,
            "reasoning_tokens": reasoning_tokens,
            "reasoning_time": reasoning_time,
            "content_tokens": content_tokens,
            "content_time": content_time,
            "overall_tokens": overall_tokens,
            "total_time": total_time
        }

    except Exception as e:
        print(f"服务商 {provider_name} 测试过程中发生错误：{e}")
        print("\n---------------------------\n")
        return None