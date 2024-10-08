provider "aws" {
  region = "ap-south-1"
}

resource "aws_lambda_function" "voice_to_text" {
  function_name = "voice_to_text"
  filename      = "function.zip"
  handler       = "app.lambda_handler"
  source_code_hash = filebase64sha256("function.zip")
  runtime       = "python3.9"
  role          = aws_iam_role.lambda_exec.arn
}

