# git-playground

This repo is a tiny Python project made for practicing common Git commands.

## 1) Clone and run

```bash
git clone <repo-url>
cd git-playground
python3 hello_world.py
```

Expected output:

```text
Hello, World!
```

## 2) Practice command checklist

### `git init`
Create a brand-new folder somewhere else on your machine and run:

```bash
mkdir my-new-git-practice
cd my-new-git-practice
git init
```

### `git status`
In this repository, check current state:

```bash
git status
```

### `git diff`
Edit `hello_world.py` (for example change `World` to your name), then run:

```bash
git diff
```

### `git add` and `git commit`
Stage and commit your change:

```bash
git add hello_world.py
git commit -m "Customize hello world output"
```

### `git push` and `git pull`
Push your branch to GitHub, then pull updates later:

```bash
git push
git pull
```

### `git checkout`
Discard local edits to a file:

```bash
git checkout -- hello_world.py
```

### `git rm`
Create a throwaway file and remove it:

```bash
echo "temporary" > remove_me.txt
git add remove_me.txt
git commit -m "Add temporary file"
git rm remove_me.txt
git commit -m "Remove temporary file"
```

### `git stash`
Make a quick edit without committing, then stash it:

```bash
git stash
git stash list
git stash pop
```

### `.gitignore`
Create files that should be ignored and observe that they do not appear in `git status`:

```bash
touch debug.log
touch .env
mkdir -p scratch && touch scratch/notes.txt
git status
```

## Suggested practice loop

1. Modify `hello_world.py`
2. Run `git status`
3. Run `git diff`
4. Stage with `git add`
5. Commit with `git commit`
6. Push with `git push`
7. Pull with `git pull`
