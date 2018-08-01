# Lab 2: ActiveGate Plugins

<br>
<br>

## Task 1: Preparing a host to monitor

### Step 1.1: Setup a Google Cloud Compute Engine instance:

Setup instance in Google:

- Name: instance-activegateplugins
- Machine type: 2vCPU (7.5 GB memory, n1-standard-2)
- Image: Debian GNU/Linux 9 (stretch)
- Allow HTTP traffic
- Allow HTTPS traffic

<br>

### Step 1.2: Connect to instance:

Connect to instance:

Copy gcloud command from Google and paste it into your terminal.

<br>

### Step 1.3: Clone repository:

Execute this command on instance-activegateplugins:

```
sudo apt-get install git
git clone https://github.com/dynatrace-innovationlab/extending-monitoring.git
```

<br>
<br>

## Task 2: Setup an ActiveGate

### Step 2.1: Setup a Google Cloud Compute Engine instance:

Setup instance in Google:

- Name: instance-activegate
- Machine type: 1vCPU (3.75 GB memory)
- Image: Windows Server 2012 R2 Datacenter (Server with Desktop Experience, x64 built on 20180710)
- Allow HTTP traffic
- Allow HTTPS traffic

<br>

### Step 2.2: Connect to instance:

Connect to instance-activegate via RDP:

Get RDP file and password from Google.

<br>

### Step 2.3: Download ActiveGate:

Download the ActiveGate installer from Dynatrace to instance-activegate.

<br>

### Step 2.4: Install ActiveGate:

You have to install the ActiveGate using the install flag: REMOTE_PLUGIN_SHOULD_INSTALL.

Execute this command on your compute engine instance:

```
C:\Users\dominik_sachsenhofer\Downloads> Dynatrace-Security-Gateway-Windows-1.149.188.exe REMOTE_PLUGIN_SHOULD_INSTALL="true"
```

<br>
<br>

## Task 3: Build and deploy an ActiveGate Plugin

### Step 3.1: Get superuser permissions:

Execute this command on instance-activegateplugins:

```
sudo su
```

<br>

### Step 3.2: Install OneAgent SDK:

Execute this command on instance-activegateplugins:

```
apt-get install python3-pip
pip3 install oneagent_sdk-1.147.90.20180611.134001-py3-none-any.whl 
```

<br>

### Step 3.3: Develop the ActiveGate plugin:

Develop the ActiveGate Plugin.

<br>

### Step 3.4: Deploy the plugin on the ActiveGate:

On instance-activegate, upload the __unzipped plugin__ folder to the __plugin_deployment directory__:

C:\Program Files\dynatrace\gateway\components\plugin_deployment\

<br>

### Step 3.5: Restart Dynatrace Remote Plugin Agent:

On instance-activegate, go to __Server Manager - Services__, search for __Dynatrace Remote Plugin Agent__ and restart the service.

<br>

### Step 3.6: Deploy the plugin on Dynatrace:

In __Dynatrace UI__, go to __Settings - Monitored technologies - Custom plugins - Upload ActiveGate plugin__

Then upload __zipped plugin__ folder to Dynatrace.

<br>

### Step 3.7: Run the demo application:

In instance-activegateplugins we run the demo app:

```
python3 -m oneagent_sdk.demo_app
```

### Step 3.8: Allow access:

Open port in Google.

<br>

### Step 3.9: Go to Dynatrace:

Go to Dynatrace, configure plugin and watch metrics coming in.
