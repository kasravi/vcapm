# Objective
The objective of this structure is to combine documentation, backlog managment, task managment, and code in single repository, in a way that it includes the overall picture and it is easy to follow as a backlog.

# Epic > Feature > Story > Task ?
Epics should contain the overall story, why we are doing things we are doing, there really isn't any best practice here. you want to go with basic what, why, who, where, how? you want to tell a story? the more close to non-developer human understanding, the better. maybe we need all these jargons, meybe we don't. let's use them when we must. not just because they are there.
So... if your mind isn't happy to work with Epic > Feature > Story > Task, define your stories right here in the root. I'll go with the hierarchy, it's fine I guess.
all I'm saying is just stick the metadata I though of on top of your readme files and the project process will be generated, use whatever hierarchy you want. 

## Epics
Here we tell the complete story and when it is appropriate we mentions the [epics](epic-name/readme.md) that together comlete the story

## Map
<!--- Table Start -->
| Type | Title | Take | Status | Progress | Tags |
|------|-------|------|--------|----------|------|
| epic | &nbsp;&nbsp;[Some cool title](./epic-name/readme.md) | Just started it | new | 10% | tag1, tag2 |
| feature | &nbsp;&nbsp;&nbsp;&nbsp;[feature's title](./epic-name/feature1/readme.md) | Looks easy | ready | 60% | tag1, tag2 |
| story | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3rd story is the charm](./epic-name/feature1/story3/readme.md) | Just started it | active | 10% |  |
| story | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[another story title](./epic-name/feature1/story2/readme.md) | Just started it | active | 10% |  |
| bug | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[bug title](./epic-name/feature1/story2/bug1/readme.md) |  | new | 0% |  |
| task | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[task title](./epic-name/feature1/story2/task1/readme.md) | Just started it | active | 30% |  |
| story | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[story title](./epic-name/feature1/story1/readme.md) | needs description | new | 0% |  |

<!--- Table End -->
