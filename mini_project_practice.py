# %% [markdown]
# # Mini Project: Hello Python — Small Experiments
# **Author:** Likith
# **Goal:** Practice basic Python in notebook form (print, math, loops, functions), document steps (Markdown), and demonstrate the same notebook runs in VS Code and Colab.
# **Date:** 2025-09-20
#
# **What this notebook contains**
# - Short explanation
# - Small math snippets
# - A loop example
# - A tiny function
# - A simple demo showing how to export this notebook to `.py` (for deployment)
#

# %%
# Hello world
print("Hello from Mini Project — running in Jupyter/Colab!")

# %% [markdown]
# ## How to run
# - Run each code cell with `Shift+Enter`.
# - In VS Code: select the Python kernel matching your interpreter.
# - In Colab: `Runtime -> Run all`.
#

# %%
# Basic math operations
a = 8
b = 3
sum_ab = a + b
prod_ab = a * b
print("a =", a, "b =", b)
print("a + b =", sum_ab)
print("a * b =", prod_ab)

# %%
# Loops & list comprehension
numbers = [1, 2, 3, 4, 5]cd
squares = []
for n in numbers:
    squares.append(n * n)
print("numbers:", numbers)
print("squares:", squares)

# %%
# same with list comprehension
squares2 = [n * n for n in numbers]
print("squares2:", squares2)

# %% [markdown]
# #Modify the loop to print only even squares.

# %%
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    if n % 2 == 0:
        squares.append(n * n)
print("numbers:", numbers)
print("squares:", squares)


# %%
def greet(name: str) -> str:
    """
    Return a greeting string for given name.
    """
    return f"Hello, {name}!"


print(greet("Likith"))


# %%
# Compute mean of list
def mean(values):
    return sum(values) / len(values) if values else None


vals = [10, 20, 30, 40]
print("values:", vals)
print("mean:", mean(vals))

# %% [markdown]
# ## Export this notebook to a Python script
# - In VS Code: Command Palette → **Jupyter: Export to Python Script** (or use the three-dot menu in notebook → Export -> Python (.py))
# - In Colab: File → Download → Download .py
#

# %% [markdown]
# ### Checklist (Mastery)
# - [ ] Ran every cell in VS Code (local kernel)
# - [ ] Ran every cell in Google Colab
# - [ ] Exported notebook to `.py` and executed that script
# - [ ] Wrote a short README describing what this notebook does
#

# %% [markdown]
#
