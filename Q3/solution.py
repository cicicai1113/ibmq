select owner_id, count(distinct_ category_id) as different_category_count from collection
group by owner_id
order by different_category_count desc;
