{{ config(materialized='table') }}

SELECT
    symbol,
    date,
    COUNT(*) AS article_count
FROM {{ ref('news_stage') }}
GROUP BY symbol, date
