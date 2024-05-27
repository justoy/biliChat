import os

# List of required environment variables and their explanations
required_env_vars = {
    "SESS_DATA": "b站的cookie SESS_DATA",
    "BILI_JCT": "b站的cookie BILI_JCT",
    "BUVID3": "b站的cookie BUVID3",
    "ROOM_ID": "b站的直播间号",
    "DASHSCOPE_API_KEY": "通义千问的api key",
    "RTMP_URL": "b站直播间推流地址"
}


# Function to check and prompt for environment variables
def check_env_vars(env_vars):
    for env_var, explanation in env_vars.items():
        if not os.getenv(env_var):
            value = input(f"环境变量 {env_var} 未设置 ({explanation})。请输入 {env_var} 的值: ")
            os.environ[env_var] = value


if __name__ == "__main__":

    # Validate environment variables
    check_env_vars(required_env_vars)

    # Example usage of the environment variables
    for var in required_env_vars:
        print(f"{var}: {os.getenv(var)}")
