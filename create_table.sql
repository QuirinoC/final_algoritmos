CREATE TABLE tweet_table (
 id BIGINT PRIMARY KEY,
 text VARCHAR NOT NULL,
 created_at VARCHAR NOT NULL,
 fake_count BIGINT,
 real_count BIGINT
);

SELECT *
FROM tweet_table
ORDER BY random()
LIMIT 1;