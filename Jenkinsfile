properties([pipelineTriggers([githubPush()])])
node{
    stage("clone"){
        git "https://github.com/aviadco11/pythonProject.git"
    }
    stage("execute"){
        bat "echo 11"
    }
}
