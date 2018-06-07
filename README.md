# Echoes From Space
### Grouping Commands with Large Scale Telemetry Data
Presented at [ICSE 2018](https://www.icse2018.org/event/icse-2018-software-engineering-in-practice-echoes-from-space-grouping-commands-with-large-scale-telemetry-data) at the Software Engineering in Practice track, in Gothenburg Sweden.

This repository contains the paper and the media accompanying the paper. The source code of the algorithms will be published soon. During the course of the follow-up work, a GUI designer tool, based on Echoes From Space, will be also published.

![Echoes from Space Poster](https://github.com/lattas/echoes-from-space/blob/master/doc/poster.jpg "Echoes from Space Poster")

### Abstract
**Background**: As evolving desktop applications continuously accrue new features and grow more complex with denser user interfaces and deeply-nested commands, it becomes inefficient to use simple heuristic processes for grouping GUI commands in multi-level menus. Existing search-based software engineering studies on user performance prediction and command grouping optimization lack evidence-based answers on choosing a systematic grouping method.

**Research Questions**: We investigate the scope of command grouping optimization methods to reduce a user’s average task completion time and improve their relative performance, as well as the benefit of using detailed interaction logs compared to sampling.

**Method**: We introduce seven grouping methods and compare their performance based on extensive telemetry data, collected from program runs of a CAD application.

**Results**: We find that methods using global frequencies, user-specific frequencies, deterministic and stochastic optimization, and clustering perform the best.

**Conclusions**: We reduce the average user task completion time by more than 17%, by running a Knapsack Problem algorithm on clustered users, training only on a small sample of the available data. We show that with most methods using just a 1% sample of the data is enough to obtain nearly the same results as those obtained from all the data. Additionally, we map the methods to specific problems and applications where they would perform better. Overall, we provide a guide on how practitioners can use search-based software engineering techniques when grouping commands in menus and interfaces, to maximize users’ task execution efficiency.

