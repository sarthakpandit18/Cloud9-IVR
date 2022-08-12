import { CognitoUserPool } from "amazon-cognito-identity-js";

const poolData = {
    UserPoolId: "us-east-1_ATtab0RhH",
    ClientId: "3pcv9390ski9ucrrki26u0r30l"
}

export default new CognitoUserPool(poolData);