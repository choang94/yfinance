SELECT name,
         SUBSTRING(ts,
         12,
         2) AS hour,
         ROUND(max(high),
         2) AS highest_price
FROM findata17
GROUP BY  SUBSTRING(ts,12,2), name
ORDER BY  highest_price DESC;