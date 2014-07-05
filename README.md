Intro-to-Hadoop-and-MapReduce
=============================

hey guys,

i'm gonna package some code i've already written for a Hadoop and MapReduce class and make it as easy to use for people as possible
the program takes a flat data file
let's say the columns are

id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score

where 
id is the id of a thread
title is the title of a thread, 
node_type can be question, answer or comment
added_at is the time of a node's creation

and finds 
- the most active forum user for each hour because users of this forum are from around the world => this can be useful if I'm Udacity and I want to find a forum moderator for the midnight to 8am EST time slot, for eg
- compute statistics such as the correlation between the length of questions and the average length of answers
- find the top n tags, find the most active users given a tag
- for each forum thread, a list of users who posted there => if one wants, I guess one can draw a social graph
- find the most used word in the forum or one of its subforums

i can use it to analyze any forum that I'm interested in, although i do not yet know 
- if i will be able to get data of a forum
- if the data will be in a similar form to the columns above (tho i suppose i can always transform data once i get them)

luckily i have a few gig of Udacity forum data so i have something :)
but it would be nice if this can be used to analyze any forum

suggestions?
i haven't thought much about 
