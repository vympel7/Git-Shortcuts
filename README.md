## Use instructions
It is as easy as running a file (*because that's actually all you have to do*)  
Execute Main.py in a terminal and you're set!

### Requires
Required | Version
---------|---------
python | >= 3.5
requests | >= 2.14.0
deprecated | any
pyjwt | any

You also need PyGithub, which you can find at https://github.com/PyGithub/PyGithub

### Commands
- [x] commands
- [x] repos
- [x] create (repo name)
- [x] fpush (repo name) (file path)
- [x] edit (repo name)
- others to come

### Use examples
Text in **bold** is printed by the computer  
Text in *italic* is user input

#### Example 1
**Enter a command:**  
*commands*  
**----- COMMANDS -----**  
**(0): commands**  
**(1): repos**  
**(2): create**  
**(3): fpush**  
**(4): edit**

#### Example 2
**Enter a command:**  
*repos*  
**----- REPOSITORIES -----**  
**(0): snakeGame**  
**(1): projectAlpha**  
**(2): minecraftPlugin**

#### Example 3
**Enter a command:**
*create projectBeta*

**Press enter to leave the parameter blank**  
**Enter the new repository description:** *sequel to projectAlpha, advanced features and better performance*  
**Enter the new repository homepage:**    
**Set repository to private (y/n)?**  
*y*  
**Automatically initialize the repository (y/n)?**  
*y*  

**Save settings as default for the next repositories [Repository name and description won't be saved] (y/n)?**  
*n*

#### Example 4
**Enter a command:**
*fpush projectBeta*

**Insert file path to push to repository projectBeta:** *Parser.go*  
**Insert a commit message:** *parser for the project*  
**Push to which branch? (leave blank for master):**   

### Useful features
Save login data to automatically login to github.  
Save repository creation data to automatically create similar repositories.


### Extra
The commands you see listed are not all the ones I'm going to add, there will be more added in the future.  
I'm open to suggestions and critiques.  
Open issues if you have any and pull requests if you want to enlarge this project.

#### Credits
All of this was made possible by the amazing Python library PyGithub, provided by @PyGithub.