# CSC14003-Fundamentals_of_Artificial_Intelligence-Group_project
 
## 1. Overview:
- This project is a part of the course CSC14003 Fundamentals of Artificial Intelligence at VNUHCM-University of Science.
- The project is call "Gem Hunter" and is implemented in Python. For more information, please read the `Project.pdf` file.
- Group members:

| Student ID | Full name |
|------------|-----------|
| 21120537 | Tran Huynh Anh Quan |
| 21120542 | Lam Hoang Quoc |
| 21120544 | Le Minh Sang |
| 21120561 | Bui Duc Thinh |


## 2. About the code in "source" folder: 
- `inputs` folder: contains the input data files for the game.
- `outputs` folder: contains the output result files for the game.
- `map_generator.py` file: 
  - Generates the map input file for the game. The choosen cell is considered Trap or Gem based on the probability
  - The result is saved in the `inputs` folder.
- `main.py` file: 
  - The main program of the game.
  - The program reads the input file, solve the game by finding if the choosen cell is Trap or Gem and write the result to the output files.
  - The result is saved in the `outputs` folder.