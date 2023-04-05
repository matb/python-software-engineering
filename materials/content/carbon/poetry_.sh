mkdir my_package
cd my_package
poetry init
poetry add numpy pandas sklearn
# write your code
poetry build
poetry publish # If configured
