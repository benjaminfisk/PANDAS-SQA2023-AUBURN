# Project Report

Our team collaborated on the main branch in the PANDAS-SQA2023-AUBURN GitHub repository. Each of our contributions are recorded in the commit history.

## Tasks

Step | Task                                                                              | Member
---- | --------------------------------------------------------------------------------- | ------
1-3  | Unpack the project; upload project as a GitHub repo; create README.md             | Ben
4.a. | Create a Git Hook that will run and report all security weaknesses in the project | Ben
4.b. | Create a fuzz.py file that will automatically fuzz 5 Python methods               | Olivia
4.c. | Integrate forensics by modifying 5 Python methods                                 | Cady
5    | Report your activities and lessons learned                                        | Team

## Activities

### Git Hook

For this task, we created a **[hook](hooks/pre-commit)** that runs bandit on repository and all of its folders recursively. The hook then pipes the output to a **[csv file](bandit_results.csv)**.<br>

### Fuzzing

For this task, we created a **[workflow](.github/workflows/software-fuzzing.yaml)** for github actions that runs a **[custom python file](KubeSec-master/fuzz.py)**. This python file creates some simple inputs and uses them to test some methods in the **[parser](KubeSec-master/parser.py)** file. The results of these tests are printed in the action as can be seen in this **[screenshot]**.<br>

### Forensics

For this task, we modified 5 methods in the **[graphtaint](KubeSec-master/graphtaint.py)** file to output data about these methods to a log file.

## Lessons Learned

Here are our main takeaways from the term project:

- Throughout the course, we learned about automation for software development and analysis, software fuzzing, and software forensics during class and with the workshops. Applying these topics to the term project was interesting, as we saw how a software developer or cybersecurity professional might use a combination of these practices for an elaborate project.
- Since our group was not from a cybersecurity background, we relied on communication and transparency with one another to grasp each of our activity topics. However, practicing effective collaboration was a rewarding experience.
- Although this speaks more to the individual part of the project, our group found the value in automated cybersecurity tools. We learned how hard-coded secrets can pose a real danger in the world of technology. It is incredibly important to develop secure, quality software.
