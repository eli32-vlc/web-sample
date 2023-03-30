import pynecone as pc

config = pc.Config(
    app_name="sample_web",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=8087,
)
