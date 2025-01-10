# Snowflake + FastAPI Template

Build RESTful APIs on top of Snowflake quickly, ish, with this FastAPI template.

### Common Files
These files I commonly come back to. I just copy and paste into a new app, I never `git clone` templates.

[snowflake.py](https://github.com/matlat8/FastAPI-Snowflake/blob/main/api/core/snowflake.py)
- Only creates connection if needed
- *Does not have connection pooling*
- global SQL query caching

[cache.py](https://github.com/matlat8/FastAPI-Snowflake/blob/main/api/core/cache.py)
- `cachefunc` decorator to cache results of functions
  - Only works if response is JSON serializable.
  - I should add passing in a custom JSON serializer