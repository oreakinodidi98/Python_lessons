IF EXIST new_folder (
    mkdir if_folder
) ELSE (
    echo "new_folder does not exist."
)
IF EXIST if_folder (
    mkdir hyperionDev
) ELSE (
    mkdir new-projects
)