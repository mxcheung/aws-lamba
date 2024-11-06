import { IAspect, IConstruct } from 'aws-cdk-lib';
import { CfnResource } from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';

class CheckNotificationsResourceHandlerAspect implements IAspect {
  visit(node: IConstruct): void {
    // Check if the construct is a `CfnResource` and matches the `AWS::Lambda::Function` logical ID pattern.
    if (node instanceof CfnResource && node.cfnResourceType === 'Custom::S3BucketNotificationsHandler') {
      console.log(`Found NotificationsResourceHandler at path: ${node.node.path}`);
      // Apply additional logic here if needed
    }
  }
}
