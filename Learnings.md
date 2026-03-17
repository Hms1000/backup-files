## The Docker Lessons I Learnt

# Base Image Error
- I used `3.11-slim` in the builder and `3.12-slim` in the runner. I think this also can contribute to compatability issues between the two stages.

# Forgot to copy source code
- In the runner stage I forgot to copy the source code from local directory to the Dockerfile. I think this had a huge impact on the failure of `CMD` because the file did not exist.

# Use of python -c
- this command, `python -c` is used to run python scripts on the command line and so by using it on `pip`, it did not work.

# pip upgrade
- I should have used `pip install` in the builder stage as they would have been a more direct way of getting the packages I needed instead I used `upgrade` which was uncenessary beacuse it will then create a cache directory that will bloat the image.

# ran pip as root
- In the runner stage pip was run as root, which is something we should always avoid for security reasons. By using a non-root user we reduce the blast radius incase of an attack.

# healthcheck
- I think at this point I should'nt have wanted to run a healthcheck because I have not transformed the file to a fastapi app.

# Ownership of the files
- I learned that `COPY --chown` gives the user ownership of the files, but the `USER` instruction is what actually tells the container to stop running as root and start running as that specific user.

# Empty `requirements.txt` file error
- At first my `requirements.txt` file was empty, so I kept on getting the error `ERROR: failed to build: failed to solve: process "/bin/sh -c pip install --no-cache-dir /wheels/*.whl" did not complete successfully: exit code: 1

Error: Process completed with exit code 1.` when pushed to github. Upon tracking I discovered that pip wasn't finding wheels to install because there was no dependencies in the `requirements.txt` file

# uvicorn[standard]
- I added `uvicorn[standard]` because it offers high perfomance unlike uvicorn alone

# ERROR: failed to build: failed to solve: dockerfile parse error on line 49:HEALTHCHECK requires at least one argument
- well this is giving me hard time I cant really figure out, why I'm gettng this error message.
- everything looks on point, but I still get this error
- I think I'm gonna have to look more closey because right now I cant see anything
- **finally**,  error solved. Docker was building the image from previously cached broken layers.
- so I added the flag `--no-cache` to my workflow and the image was succecfully built
