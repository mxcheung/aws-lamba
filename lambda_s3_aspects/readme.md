
Using a custom aspect, 
you can automatically apply VPC configurations to all Lambda functions that meet certain criteria. 
In this case, we’ll attach the VPC configuration to Lambda functions as required.

Interface appears to adopt vistor pattern
```
// Custom aspect to enforce VPC on Lambda functions to traverse nodes or constructs.
class LambdaVpcAspect implements cdk.IAspect {

  visit(node: IConstruct): void {
    if (node instanceof lambda.Function) {

```
