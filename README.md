# Kindle-Klock

Simple clock app designed (currently) for the 10th generation base Kindle

This app is currently in the most early of early development, and **__WILL NOT WORK__**

## Configuration
When configureing your weather setting you must create a userConfig.json file inside of the kindle-klock-src folder it will look something like this

``` json
{
    "weather": {
        "longitude": "[longitude]",
        "latitude": "[latitude]",
        "wind-speed-unit": "[ms or mph or kn]",
        "temperature-unit": "[fahrenheit or celsius]",
        "precipitation-unit": "[inch or millimeter]"
    }
}
```