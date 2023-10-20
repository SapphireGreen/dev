<h3> Follow the steps to upload large file into github. </h3>

# Step 1, Install the lfs module from github using the following commnad. 

`$ git lfs install`

# Step 2, track the large file in your repository.

`$ git lfs track "*.psd"`

# Note - Above command is used to track multiple file with .psd extension, you can track single file as well. 

# step 3, lfs file is tracked using ".gitattributes". 

`$ git add .gitattributes`

# step 4, to commit the file to remote repository use the below set of command. 

`$ git add sample.psd`
`$ git commit -m "Added design file"`
`$ git push origin master`

# this should successfully upload the file to remote repository. 

