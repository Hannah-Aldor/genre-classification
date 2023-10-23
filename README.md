# genre-classification
Final project for ECS 171. Under construction...

1) Download project
2) cd to project directory in terminal
3) Run the following commands, making sure to replace the [full project path] with your own project path:
docker build -t 171_group_project .
docker run -v [full project path]/data/train.csv:/app/data/data.csv -v [full project path]/output_da.json:/app/output/output_da.json 171_group_project "da.py" /app/data/data.csv /app/output/output_da.json
docker run -v [full project path]/output_da.json:/app/config/config.json -v [full project path]/output.json:/app/output/output.json -v [full project path]/data/train.csv:/app/data/data.csv 171_group_project "dq.py" /app/config/config.json /app/output/output.json /app/data/data.csv

4) output_da.json has the dq test cases
5) output.json has the output of running the test cases on the csv file
