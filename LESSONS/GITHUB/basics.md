# GitHub and Git Setup - Notes

## 1. Check version
- check the version to confirm Git is installed:
  ```bash
  git --version

## 2. Set Up Git with Your Identity
- Configure your Git username and email: 
    ```bash
    git config --global user.name "Your Name"  
    git config --global user.email "your_email@example.com"

## 3. Create a GitHub Repository
Go to GitHub and create a new repository:  
Example: https://github.com/TheEngineer42/TheEngineer42.git

## 4. Connect Your Local Folder to GitHub
- Open Git Bash and navigate to the local project folder:
    ```bash  
    cd "C:/path/to/your/project"

- Initialize a new Git repository in the folder:
    ```bash
    git init

- Add the GitHub remote repository:
    ```bash
    git remote add origin https://github.com/TheEngineer42/TheEngineer42.git

## 5. Push Local Files to GitHub
- Add all files in your project folder to Git:
    ```bash
    git add .

- Commit the changes:
    ```bash
    git commit -m "Initial commit"
    

- Push the files to the remote GitHub repository:
    ```bash
    git push -u origin main

## 6. Work on New Changes
- After making changes to your code, repeat the following steps to push updates:  

- 1. Stage the changes:
    ```bash
    git add .

- 2. Commit the changes:
    ```bash
    git commit -m "Updated files"

    

- 3. Push the changes:
    ```bash
    git push origin main

## 7. Managing Branches
- If you want to delete the master branch and switch to main, follow these steps:


1. Switch to the main branch locally:
    ```bash
    git checkout main

2. Delete the master branch locally:
    ```bash
    git branch -d master

3. Delete the master branch remotely (on GitHub):
    ```bash
    git push origin --delete master

4. Set main as the default branch on GitHub:
- Go to Settings > Branches > Default branch > Select main.

## 8. Fixing Merge Conflicts
- If a merge conflict occurs, you'll see a message like:
    ```bash
    fatal: refusing to merge unrelated histories


To resolve merge conflicts.
1. Use git pull to pull the changes:
    ```bash
    git pull origin main --allow-unrelated-histories


2. Resolve conflicts manually in your code editor (e.g., VS Code).

3. Stage the resolved files:
    ```bash
    git add <file>

4. Commit the resolution:
   ```bash
    git commit -m "Resolved merge conflicts"

5. Push the changes to GitHub:
    ```bash
    git push origin main


## 9. Working in VS Code with Git

Source Control in VS Code: You can also use the Source Control panel in VS Code to commit and push changes to GitHub directly.
Changes are tracked automatically, and you can:
Stage files
Commit changes
Push/pull directly from within VS Code







    


