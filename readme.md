# Objective
The objective of this structure is to combine documentation, backlog managment, task managment, and code in single repository, in a way that it includes the overall picture and it is easy to follow as a backlog.

# Epic > Feature > Story > Task ?
Epics should contain the overall story, why we are doing things we are doing, there really isn't any best practice here. you want to go with basic what, why, who, where, how? you want to tell a story? the more close to non-developer human understanding, the better. maybe we need all these jargons, meybe we don't. let's use them when we must. not just because they are there.
So... if your mind isn't happy to work with Epic > Feature > Story > Task, define your stories right here in the root. I'll go with the hierarchy, it's fine I guess.
all I'm saying is just stick the metadata I though of on top of your readme files and the project process will be generated, use whatever hierarchy you want. 

## Epics
Here we tell the complete story and when it is appropriate we mentions the [epics](e/epic-name/readme.md) that together comlete the story

<!--- Table Start -->
<table><thead><tr><th>Type</th><th>Title</th><th>Take</th><th>Status</th><th>Progress</th><th>Tags</th></tr></thead><tbody><tr style="color: green;"><td> epic </td><td> <a href='./e/epic-name/readme.md'>Some cool title</a> </td><td> Just started it </td><td> new </td><td> 10% </td><td> tag1, tag2 </td></tr><tr><td> feature </td><td> &nbsp;&nbsp;<a href='./e/epic-name/e/feature1/readme.md'>feature's title</a> </td><td> Looks easy </td><td> ready </td><td> 60% </td><td> tag1, tag2 </td></tr><tr><td> story </td><td> &nbsp;&nbsp;&nbsp;&nbsp;<a href='./e/epic-name/e/feature1/e/story3/readme.md'>3rd story is the charm</a> </td><td> Just started it </td><td> active </td><td> 10% </td><td>  </td></tr><tr><td> story </td><td> &nbsp;&nbsp;&nbsp;&nbsp;<a href='./e/epic-name/e/feature1/e/story2/readme.md'>another story title</a> </td><td> Just started it </td><td> active </td><td> 10% </td><td>  </td></tr><tr><td> bug </td><td> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='./e/epic-name/e/feature1/e/story2/e/bug1/readme.md'>bug title</a> </td><td>  </td><td> new </td><td> 0% </td><td>  </td></tr><tr><td> task </td><td> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='./e/epic-name/e/feature1/e/story2/e/task1/readme.md'>task title</a> </td><td> Just started it </td><td> active </td><td> 30% </td><td>  </td></tr><tr><td> story </td><td> &nbsp;&nbsp;&nbsp;&nbsp;<a href='./e/epic-name/e/feature1/e/story1/readme.md'>story title</a> </td><td> needs description </td><td> new </td><td> 0% </td><td>  </td></tr></tbody></table>
<!--- Table End -->
