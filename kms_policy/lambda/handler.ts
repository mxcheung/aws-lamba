import { SecretsManager } from 'aws-sdk';

export const handler = async (event: any): Promise<any> => {
    const secretName = "mySecret";
    const region = "us-west-2";

    const client = new SecretsManager({ region: region });

    try {
        const data = await client.getSecretValue({ SecretId: secretName }).promise();
        
        if ('SecretString' in data) {
            const secret = data.SecretString;
            console.log(`Secret: ${secret}`);
        } else {
            const decodedBinarySecret = Buffer.from(data.SecretBinary as string, 'base64').toString('ascii');
            console.log(`Binary Secret: ${decodedBinarySecret}`);
        }
    } catch (err) {
        console.error(`Error retrieving secret: ${err}`);
    }

    return {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
};
