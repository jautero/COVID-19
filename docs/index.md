This page was last updated at {{ "now" | date: "%Y-%m-%d %H:%M" }}.

This page was last updated at {{ "now" | date: "%Y-%m-%d %H:%M" }}.

<script>
    function toggle_avg(checkbox) {
        if (checkbox.checked) {
            searchvalue=".png";
            newvalue="_c14davg.png";
        } else {
            searchvalue="_c14davg.png";
            newvalue=".png";
        }
        images=document.getElementsByTagName("img")
        for(var i=0; i< images.length; i++) {
            images[i].src=images[i].src.replace(searchvalue,newvalue);
        }
    }
</script>

<input type="checkbox" onchange="toggle_avg(this);" checked> Use 14 day average
## Confirmed infections

### Top 10 Countries

![Graph of infections of top 10 countries](confirmed_c14davg.png)

![Graph of infections of top 10 countries](confirmed_EU_c14davg.png)

![Graph of infections of top 10 countries](confirmed_Nordics_c14davg.png)

### Top 10 US States

![Graph of infections of top 10 US states](confirmed_US_c14davg.png)

## Deaths

### Top 10 Countries

![Graph of deaths of top 10 countries](deaths_c14davg.png)

![Graph of infections of top 10 countries](deaths_EU_c14davg.png)

![Graph of infections of top 10 countries](deaths_Nordics_c14davg.png)

### Top 10 US States

![Graph of deaths of top 10 US states](deaths_US_c14davg.png)

## Current infections

Johns Hopkins has data for confirmed cases, deaths and recoveries. When
deaths and recoveries are subtracted from confirmed cases, we get estimate 
of current infections. The advantage is that this is not cumulative and
produces downward trend when the peak of epidemy is passed.

> There is something strange happening to Spain's figures. Probably
> yesterday's data for recovered was missing causing miscalculation.

### Top 10 Countries

![Graph of infected of top 10 countries](infected_c14davg.png)

![Graph of infections of top 10 countries](infected_EU_c14davg.png)

![Graph of infections of top 10 countries](infected_Nordics_c14davg.png)

### Countries that seem to have passed peak of epidemy

{% include_relative peaked.md %}
