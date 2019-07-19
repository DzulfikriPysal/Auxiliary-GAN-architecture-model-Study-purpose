from discriminator import *
from generator import *

print("=====================================================================================")
print("Discriminator Summary")
print("=====================================================================================")
model_discriminator = define_discriminator()
model_discriminator.summary()

print("=====================================================================================")
print("")
print("")


print("=====================================================================================")
print("Generator Summary")
print("=====================================================================================")

latent_dim = 100
model_generator = define_generator(latent_dim)
model_generator.summary()