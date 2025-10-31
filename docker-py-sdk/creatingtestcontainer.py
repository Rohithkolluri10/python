import docker

try:
    client = docker.from_env()
    print("Docker client created successfully.")
except Exception as e:
    print(f"Error creating Docker client: '{e}'")
    exit(1)

# Configuring the container
container_image = "alpine:latest"
container_command  = "echo hello world"

print(f"Running the Docker image with the : {container_command}")

# Running the container
# using the remove , detach options

try:
    container_output = client.containers.run(
        image=container_image,
        command=container_command,
        remove=True,
        detach=False,
        stdout=True,
        stderr=True
    )

    print("Container output:")
    print(container_output.decode("utf-8").strip())
    print("-----------------------------------/n")
    print("Container ran successfully.")

except docker.errors.ImageNotFound:
  print(f"Error: The specified image '{container_image}' was not found.")
except Exception as e:
  print(f"Error running the container: {e}")

