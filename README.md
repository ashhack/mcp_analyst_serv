# mcp_analyst_serv
MCP Server with Prompt, Tools for Analytics

## CI/CD with GitHub Actions

This project uses GitHub Actions for continuous integration and deployment:

### CI Workflow

The CI workflow (`ci-cd.yml`) runs on every push to the main branch and on pull requests to main. It:

1. Sets up Python 3.13
2. Installs dependencies
3. Runs linting with ruff
4. Validates that the server can start

### Deployment Workflow

The deployment workflow (`deploy.yml`) runs after the CI workflow completes successfully on the main branch. It:

1. Sets up Python 3.13
2. Installs dependencies
3. Builds the package
4. Contains placeholder steps for deployment

### Customizing Deployment

To customize the deployment for your specific environment:

1. Edit `.github/workflows/deploy.yml`
2. Uncomment and configure one of the example deployment methods or add your own
3. Set up any necessary secrets in your GitHub repository settings

Example deployment targets include:
- Server via SSH
- AWS
- Azure
- Google Cloud
- Heroku
