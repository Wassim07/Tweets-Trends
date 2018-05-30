// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.

export const environment = {
  production: false,

  firebase: {
    apiKey: "AIzaSyB8cdgxttEr0HzG108oO2qaLLiwvY1FKzk",
    authDomain: "tweets-trends.firebaseapp.com",
    databaseURL: "https://tweets-trends.firebaseio.com",
    projectId: "tweets-trends",
    storageBucket: "tweets-trends.appspot.com",
    messagingSenderId: "568444102478"
  }
};
