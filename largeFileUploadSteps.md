<h3> Follow the steps to upload large file into github. </h3>

<h4> Step 1, Install the lfs module from github using the following commnad. </h4>

`$ git lfs install`

<h4> Step 2, track the large file in your repository.</h4>

`$ git lfs track "*.psd"`

<h4>Note - Above command is used to track multiple file with .psd extension, you can track single file as well.</h4> 

<h4>step 3, lfs file is tracked using ".gitattributes". </h4>

`$ git add .gitattributes`

<h4>step 4, to commit the file to remote repository use the below set of command. </h4>

`$ git add sample.psd`
`$ git commit -m "Added design file"`
`$ git push origin master`

<h5>this should successfully upload the file to remote repository. </h5>

