## The Docker Lessons I Learnt

# Base Image Error
- I used `3.11-slim` in the builder and `3.12-slim` in the runner. I think this also can contribute to compatability issues between the two stages.

# Forgot to copy source code
- In the runner stage I forgot to copy the source code from local directory to the Dockerfile. I think this had a huge impact on the failure of `CMD` because the file did not exist.

# Use of python -c
- this command, `python -c` is used to run python scripts on the command line and so by using it on `pip`, it did not work.

# pip upgrade
- i should have used `pip install` in the builder stage as they would have been a more direct way of getting the packages I needed instead I used `upgrade` which was uncenessary beacuse it will then create a cache directory that will bloat the image.

# ran pip as root
- In the runner stage pip was run as root, which is something we should always avoid for security reasons. By using a non-root user we reduce the blast radius incase of an attack.

# healthcheck
- I think at this point I should'nt have wanted to run a healthcheck because I have not transformed the file to a fastapi app.