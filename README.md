# CICD Lab
## Task

Objectives
1. Set up a GitHub repository (Set to public to enable environments): tm-<name>-cicd-lab
2. Create a simple python script that:
- Accepts 2 parameters (num_a,num_b)
- Print the values of the parameters, the sum, and secret derived from env var
3. Create 2 Github Environment Group w/ these settings:
- NUM_A 	= 1 		| 10
- NUM_B 	= 2 		| 20
- SECRET 	= secret1| secret2
4. Create 2 Github Action Workflows with steps:
- Uses templates
- Runs your python script (hint: install)
- Runs CLI command to print unencrypted secret value (hint: | sed ‘s/./& /g’)
- In this order
5. Run Github actions for both workflows

## Output
### Environments
  **test-dev**
  - Environment Variables
      - NUM_A = 1
      - NUM_B = 2
  - Environment secrets
      SECRET = secret1
  
  **test-uat**
  - Environment Variables
      - NUM_A = 10
      - NUM_B = 20
  - Environment secrets
      SECRET = secret2
### Workflows

**test dev workflow**

  ![image](https://github.com/user-attachments/assets/72b5b108-ec65-4adc-a59b-7005c17fb305)
  ![image](https://github.com/user-attachments/assets/d32a0d5b-8b63-4412-b1e4-03d41e0d29fd)
  ![image](https://github.com/user-attachments/assets/e8ee4b07-2a8f-4aab-9e92-b6cfc27fa2c1)

**test aut workflow**

  ![image](https://github.com/user-attachments/assets/6f398432-2cdf-4d47-b115-ab66cfbbb8cb)
  ![image](https://github.com/user-attachments/assets/86882069-5395-4b1c-8538-27990a12e4e8)
  ![image](https://github.com/user-attachments/assets/45e9ead3-05d6-4b5a-b0e6-d52acd8b06cc)



