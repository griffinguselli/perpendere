# Perpendere
> ### Perpendere
>Verb. /pɛrˈpɛn.dɛ.rɛ/


A Python project used to assign, search and store values!
## Installation
You Need Python installed first. Check With:
```bash
python3 --version
```
If it returns a number (like 3.12.3), you have it installed. Otherwise, install with:
#### Debian/Ubuntu Base (apt)
```bash
sudo apt install python3
```
#### Arch Base (pacman)
```bash
sudo pacman -S python
```
#### macOS (homebrew)
```bash
brew install python3
```
#### Windows (winget)
```bash
winget install Python.Python.3
```
Now that python3 is installed, install the python file. Make sure that perpendere.py is in your Home folder. Now create the function.
#### Debian/Ubuntu Base:
```bash
echo 'perpendere() { python3 ~/diction.py "$@"; }' >> ~/.bashrc && source ~/.bashrc
```
#### Arch Base:
```bash
echo 'perpendere() { python3 ~/diction.py "$@"; }' >> ~/.zshrc && source ~/.zshrc
```
#### macOS:
```base
echo 'perpendere() { python3 ~/diction.py "$@"; }' >> ~/.zshrc && source ~/.zshrc
```
#### Windows:
```bash
Add-Content $PROFILE 'function perpendere { python ~/diction.py $args }'
```
( If profile doesn't exist yet, Paste:)
```bash
New-Item -Path $PROFILE -Force
```
## Usage
### Assign
```bash
perpendere 1 key value
```
or

```bash
perpendere 1 "long key" "long value"
```
This puts it into the dict.csv file that converts into a python dictionary.

### Search
```bash
 perpendere 0 key
```
or
```bash
perpendere 0 "long key"
```
