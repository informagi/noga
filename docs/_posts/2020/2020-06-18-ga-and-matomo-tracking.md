---
layout: "post"
title: "Google Analytics and Matomo tracking in depth"
author: "Marnix Dessing"
date: "2020-06-18 17:00"
excerpt: "Google Analytics and Matomo tracking in depth"
tags: NoGA "Web analytics"
---
# Google Analytics and Matomo tracking in depth
This pages sets the goal of giving a detailed description of the tracking implementations of Google Analytics and Matomo. We have concluded that there are [four main tracking techniques](/techniques) and we will now deep dive into the implementation of both tools. 

## Google Analytics
Google published a tracking code overview for their Web Analytics platform. It explains that the platform exploits the JavaScript tag technique[1]. The tracking code works in three steps:
1. The browser loads the JavaScript tracking code on a tracked web page.
2. The script collects the required data. This is configurable using a command query in the JavaScript execution.
3. After the data is collected the data is send to Google Analytics trough a GIF (1x1 pixel image) request. All data is contained in the URL parameters of that request.

### Cookie usage
Google explains that first-party cookies are used for[2]:
* Determine which domain to measure.
* Distinguish unique users.
* Throttle the request rate.
* Remember the number and time of previous visits.
* Remember traffic source information.
* Determine the start and end of a session.
* Remember the value of visitor-level custom variables.

By default, cookies are set on the domain specified in the document.host browser property and the cookie path is set to the root level (/).

However, if one chooses to enable advertising features, third-party cookies are set[1]. Those third-party cookie domains are set to the domains of different google marketing products such as: DoubleClick.net, gstatic.com etc.[3] This kind of third-party cookie can be used to track users across the web. For each site containing a reference to one of these domains the cookie is send to Google. (See HTTP Cookies)

### User identification
User identification over multiple sessions is done via the first-party cookie. Which contains a random generated ID (the client ID) to identify a user. Google Analytics also provides a feature to use a custom user ID besides the client ID. One problem this overcomes is tracking the same user across different browsers and devices (when the user ID is known and provided). By only using the client ID it is not possible to recognize the same user on different browsers or devices. [4]


### Collected data
The parameters of the GIF request described above, have been documented by Google[5] a overview of parameters is displayed below.

|Variable| Description |
|--------|-------------|
| utmac  | Account String. Appears on all requests.
| utmcc  | Cookie values. This request parameter sends all the cookies requested from the page. |
| utmcn  | Starts a new campaign session. Either utmcn or utmcr is present on any given request. Changes the campaign tracking data; but does not start a new session
| utmcr  | Indicates a repeat campaign visit. This is set when any subsequent clicks occur on the same link. Either utmcn or utmcr is present on any given request.
| utmcs  | Language encoding for the browser. Some browsers don't set this, in which case it is set to "-"
| utmdt  | Page title, which is a URL-encoded string.|
| utme   | Extensible Parameter 	Value is encoded. Used for events and custom variables. | 
| utmfl  | Flash Version |
| utmhn  | Host Name, which is a URL-encoded string. |
| utmhid | A random number used to link Analytics GIF requests with Google AdSense.
| utmipc | Product Code. This is the sku code for a given product. |
| utmipn | Product Name, which is a URL-encoded string. | 	
| utmipr | Unit Price. Set at the item level. Value is set to numbers only in U.S. currency format. |
| utmiqt | Quantity. |
| utmiva | Variations on an item. For example: large, medium, small, pink, white, black, green. String is URL-encoded. | 
| utmje  | Indicates if browser is Java-enabled. 1 is true. |
| utmn   | Unique ID generated for each GIF request to prevent caching of the GIF image. |
| utmp   | Page request of the current page. | 
| utmr   | Referral, complete URL. | 	
| utmsc  | Screen color depth | 	
| utmsr  | Screen resolution | 
| utmt   | Indicates the type of request, which is one of: event, transaction, item, or custom variable. If this value is not present in the GIF request, the request is typed as page. | 
| utmtci | Billing City | 
| utmtco | Billing Country |
| utmtid | Order ID, URL-encoded string. |
| utmtrg | Billing region, URL-encoded string.	|
| utmtsp | Shipping cost. Values as for unit and price.|
| utmtst | Affiliation. Typically used for brick and mortar applications in ecommerce. |
| utmtto | Total. Values as for unit and price. |
| utmttx | Tax. Values as for unit and price. | 
| utmul  | Browser language. |
| utmwv  | Tracking code version | 


## Matomo
Matomo, just as Google Analytics, uses a JavaScript tag tracking technique. However, Matomo is equipped with other tools too. 

When no JavaScript execution is possible, Matomo can use a web beacon instead[6]. Both the JavaScript and Web Beacon can be used depending on the browser of the user. The Web Beacon can also be used to track the reading of emails (that is, if the mail client does not block the beacon)[7].

Another feature is the log import feature for user tracking. Mainly aimed to protect privacy of users by replacing the front-end techniques. Examples given of sites on which privacy is highly important are government or healthcare portals. I.e. on sites with webpages that may contain sensitive information it can violate privacy rights of users to use Javascript tracking (content tracking for example). 

Matomo also offers IP anonymisation, respects can DoNotTrack requests and has other privacy features.[8] Both for Javascript tracking and log importation.

### Cookie usage
Matomo uses first-party cookies only. Unless it is configured to place a third-party cookie[9] which can be configured when tracking over multiple domains for example.

The first-party cookies are listed in the documentation (by name, time to live and details)[9]:
* _pk_id, - 13 months (used to store a few details about the user such as the unique visitor ID)
* _pk_ref, - 6 months (used to store the attribution information, the referrer initially used to visit the website)
* _pk_ses, _pk_cvar, _pk_hsr - 30 minutes (short lived cookies used to temporarily store data for the visit)
* _pk_testcookie, is created and should be then directly deleted (used to check whether the visitor’s browser supports cookies)
* mtm_consent, is created with no expiry date to forever remember that consent was given by the user. It is possible to define an optional expiry period for your user consent by (...).

It is possible to disable cookie usage in Matomo. Matomo will fall back on other identification methods such as browser fingerprint. The cost of not using cookies is loss in data accuracy, reports such as "Days since last visits" or "Visit by visit count" will be affected[10].

### User identification
Matomo has several options to identify new or returning users[11]:
1. If a User ID is set (in API) the visitor ID is derived (hashed) and matched against known visitor IDs. If no match is found the visitor fingerprint is matched against known fingerprints. 
2. When a Visitor ID was manually set this ID is matched against known visitor IDs.
3. Cookies 
    1. If trust_visitors_cookies is configured, when a visitor ID is found in a cookie (1st or 3th party) this visitor ID is matched against known visitor IDs.
    2. Otherwise when a visitor ID is found in a cookie (1st or 3th party) this visitor ID is matched against known visitor IDs. If no match is found the visitor fingerprint is matched against known fingerprints. 
    3. Finally, if no visitor ID is found in the cookie (1st or 3th party) and a visitor ID was not specified, the visitor fingerprint is matched against known fingerprints.

### Collected data
Matomo defines the following list of data that is tracked by default[12]:
* User IP address*
* Optional User ID*
* Date and time of the request
* Title of the page being viewed (Page Title)
* URL of the page being viewed (Page URL)*
* URL of the page that was viewed prior to the current page (Referrer URL)*
* Screen resolution being used
* Time in local user’s timezone
* Files that were clicked and downloaded (Download)
* Links to an outside domain that were clicked (Outlink)
* Pages generation time (the time it takes for webpages to be generated by the webserver and then downloaded by the user: Page speed)
* Location of the user: country, region, city, approximate latitude and longitude (Geolocation)*
* Main Language of the browser being used (Accept-Language header)
* User Agent of the browser being used (User-Agent header)

Bullet points market with a asterisk (*) are mentioned as data possible containing Personally Identifiable Information (PII). Besides the marked points above, the follwing list is also data that can contain PII.
* Custom detentions and custom variables
* Site searches
* E-commerce order id
* Tracking cookie IDs
* Heatmaps and session recordings

#### Downloads
The tracking of downloads is not always registered with Google Analytics, at least not by default. Matomo provides features for automatically registering downloads. This works by detecting links to a file (based on the file extension in the URL). If a URL does not always contain a file extension a work around is to add a CSS class to the link. This will register the link as a download in Matomo. [13]

## GIF request
Both Google Analytics and Matomo use a GIF image sized 1x1 to send the collected data to the backend. In search for an answer on the question why a GIF image is used the first main suspect was Cross-origin-resource-sharing (CORS). As the JavaScript often is executed from a different origin then the origin of the actual web analytics service. The fact that images can be loaded from any domain without CORS makes a tiny GIF image suitable for cross-origin requests. The GIF image is never rendered to the DOM and is only retrieved by the JavaScript. [16]

## Http cookies
Cookies are used to maintain a form of state between client (a visitors browser) and server. Cookies are set by the Server via HTTP or via JavaScript. The cookie is then send along on each request to the server [14].

| Cookie setting | Description                                                                  |
|:---------------|:-----------------------------------------------------------------------------|
| Name           | The name of the cookie.                                                      |
| Expires        | The expiration date and time.                                                |
| Secure         | If set the cookie is send over HTTPS only.                                   |
| HttpOnly       | If set the cookie is inaccessible with JavaScript.                           |
| Domain         | The domain on which the cookie is active.                                    |
| Path           | The path within the domain in which the cookie is active '/' is the root.    |

### First and Third-party cookies
The distinction between first and third-party cookies is important in the field of Web Analytics and tracking. Third-party cookies are mostly used for advertising and tracking. Browsers and add-ons such as ad-block are now often blocking third-party cookies. 

For cookies placed by a website that is being browsed (lets say example.com), a cookie with the domain example.com is a first-party cookie. A cookie with another domain e.g. doubleclick.net is a third-party cookie. This third-party cookie can be placed by an ad or banner that is loaded onto the page. Now a user can be identified on other websites with a ad or banner from that same third-party domain [15].


## References
[1] [Overview tracking code](https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview)

[2] [Google analytics cookies](https://developers.google.com/analytics/devguides/collection/analyticsjs/cookie-usage?hl=nl)

[3] [Google cookie usage](https://policies.google.com/technologies/types?hl=nl )

[4] [User identification of GA](https://developers.google.com/analytics/devguides/collection/analyticsjs/cookies-user-id)

[5] [What data does GA track?](https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview#gifParameters)

[6] [Beacon usage](https://matomo.org/faq/general/when-tracking-visitors-using-an-image-beacon-instead-of-the-javascript-tracker-what-are-the-differences/)

[7] [Tracking without javascript](https://matomo.org/faq/how-to/faq\_176/)

[8] [Log importing and analysis ](https://matomo.org/log-analytics/)

[9] [JavaScript cookies](https://matomo.org/faq/general/faq\_146/)

[10] [No Cookies](https://matomo.org/faq/general/faq\_156/)

[11] [Unique visitor recognition](https://matomo.org/faq/general/#faq\_21418)

[12] [What data does Matomo track? ](https://matomo.org/faq/general/faq\_18254/)

[13] [Tracking downloads](https://matomo.org/faq/new-to-piwik/faq\_47/)

[15] [Http cookies mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

[16] [Cross-origin-resource-sharing](https://developer.mozilla.org/nl/docs/Web/HTTP/CORS)
