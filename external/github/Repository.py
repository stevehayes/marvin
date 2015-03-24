# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Christopher Gilbert <christopher.john.gilbert@gmail.com>      #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Adrian Petrescu <adrian.petrescu@maluuba.com>                 #
# Copyright 2013 Mark Roddy <markroddy@gmail.com>                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
# ##############################################################################

import urllib.request, urllib.parse, urllib.error
import datetime

import github.GithubObject
import github.PaginatedList

import github.Branch
import github.IssueEvent
import github.ContentFile
import github.Label
import github.GitBlob
import github.Organization
import github.GitRef
import github.Issue
import github.Repository
import github.PullRequest
import github.RepositoryKey
import github.NamedUser
import github.Milestone
import github.Comparison
import github.CommitComment
import github.GitCommit
import github.Team
import github.Commit
import github.GitTree
import github.Hook
import github.Tag
import github.GitTag
import github.Download
import github.Permissions
import github.Event
import github.Legacy
import github.StatsContributor
import github.StatsCommitActivity
import github.StatsCodeFrequency
import github.StatsParticipation
import github.StatsPunchCard


class Repository(github.GithubObject.CompletableGithubObject):
    """
    This class represents Repositorys. The reference can be found here http://developer.github.com/v3/repos/
    """

    @property
    def archive_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._archive_url)
        return self._archive_url.value

    @property
    def assignees_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._assignees_url)
        return self._assignees_url.value

    @property
    def blobs_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._blobs_url)
        return self._blobs_url.value

    @property
    def branches_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._branches_url)
        return self._branches_url.value

    @property
    def clone_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._clone_url)
        return self._clone_url.value

    @property
    def collaborators_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._collaborators_url)
        return self._collaborators_url.value

    @property
    def comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def commits_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commits_url)
        return self._commits_url.value

    @property
    def compare_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._compare_url)
        return self._compare_url.value

    @property
    def contents_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._contents_url)
        return self._contents_url.value

    @property
    def contributors_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._contributors_url)
        return self._contributors_url.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def default_branch(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._default_branch)
        return self._default_branch.value

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def downloads_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._downloads_url)
        return self._downloads_url.value

    @property
    def events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    def fork(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._fork)
        return self._fork.value

    @property
    def forks(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._forks)
        return self._forks.value

    @property
    def forks_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._forks_count)
        return self._forks_count.value

    @property
    def forks_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._forks_url)
        return self._forks_url.value

    @property
    def full_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._full_name)
        return self._full_name.value

    @property
    def git_commits_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._git_commits_url)
        return self._git_commits_url.value

    @property
    def git_refs_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._git_refs_url)
        return self._git_refs_url.value

    @property
    def git_tags_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._git_tags_url)
        return self._git_tags_url.value

    @property
    def git_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._git_url)
        return self._git_url.value

    @property
    def has_downloads(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._has_downloads)
        return self._has_downloads.value

    @property
    def has_issues(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._has_issues)
        return self._has_issues.value

    @property
    def has_wiki(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._has_wiki)
        return self._has_wiki.value

    @property
    def homepage(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._homepage)
        return self._homepage.value

    @property
    def hooks_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._hooks_url)
        return self._hooks_url.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def issue_comment_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._issue_comment_url)
        return self._issue_comment_url.value

    @property
    def issue_events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._issue_events_url)
        return self._issue_events_url.value

    @property
    def issues_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._issues_url)
        return self._issues_url.value

    @property
    def keys_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._keys_url)
        return self._keys_url.value

    @property
    def labels_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._labels_url)
        return self._labels_url.value

    @property
    def language(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._language)
        return self._language.value

    @property
    def languages_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._languages_url)
        return self._languages_url.value

    @property
    def master_branch(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._master_branch)
        return self._master_branch.value

    @property
    def merges_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._merges_url)
        return self._merges_url.value

    @property
    def milestones_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._milestones_url)
        return self._milestones_url.value

    @property
    def mirror_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._mirror_url)
        return self._mirror_url.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def network_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._network_count)
        return self._network_count.value

    @property
    def notifications_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._notifications_url)
        return self._notifications_url.value

    @property
    def open_issues(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._open_issues)
        return self._open_issues.value

    @property
    def open_issues_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._open_issues_count)
        return self._open_issues_count.value

    @property
    def organization(self):
        """
        :type: :class:`github.Organization.Organization`
        """
        self._completeIfNotSet(self._organization)
        return self._organization.value

    @property
    def owner(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._owner)
        return self._owner.value

    @property
    def parent(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._parent)
        return self._parent.value

    @property
    def permissions(self):
        """
        :type: :class:`github.Permissions.Permissions`
        """
        self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    def private(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._private)
        return self._private.value

    @property
    def pulls_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._pulls_url)
        return self._pulls_url.value

    @property
    def pushed_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._pushed_at)
        return self._pushed_at.value

    @property
    def size(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._size)
        return self._size.value

    @property
    def source(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._source)
        return self._source.value

    @property
    def ssh_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._ssh_url)
        return self._ssh_url.value

    @property
    def stargazers_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._stargazers_count)  # pragma no cover (Should be covered)
        return self._stargazers_count.value  # pragma no cover (Should be covered)

    @property
    def stargazers_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._stargazers_url)
        return self._stargazers_url.value

    @property
    def statuses_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._statuses_url)
        return self._statuses_url.value

    @property
    def subscribers_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._subscribers_url)
        return self._subscribers_url.value

    @property
    def subscription_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._subscription_url)
        return self._subscription_url.value

    @property
    def svn_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._svn_url)
        return self._svn_url.value

    @property
    def tags_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._tags_url)
        return self._tags_url.value

    @property
    def teams_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._teams_url)
        return self._teams_url.value

    @property
    def trees_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._trees_url)
        return self._trees_url.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def watchers(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._watchers)
        return self._watchers.value

    @property
    def watchers_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._watchers_count)
        return self._watchers_count.value

    def add_to_collaborators(self, collaborator):
        """
        :calls: `PUT /repos/:owner/:repo/collaborators/:user <http://developer.github.com/v3/repos/collaborators>`_
        :param collaborator: string or :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser) or isinstance(collaborator, str), collaborator

        if isinstance(collaborator, github.NamedUser.NamedUser):
            collaborator = collaborator._identity

        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/collaborators/" + collaborator
        )

    def compare(self, base, head):
        """
        :calls: `GET /repos/:owner/:repo/compare/:base...:head <http://developer.github.com/v3/repos/commits>`_
        :param base: string
        :param head: string
        :rtype: :class:`github.Comparison.Comparison`
        """
        assert isinstance(base, str), base
        assert isinstance(head, str), head
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/compare/" + base + "..." + head
        )
        return github.Comparison.Comparison(self._requester, headers, data, completed=True)

    def create_git_blob(self, content, encoding):
        """
        :calls: `POST /repos/:owner/:repo/git/blobs <http://developer.github.com/v3/git/blobs>`_
        :param content: string
        :param encoding: string
        :rtype: :class:`github.GitBlob.GitBlob`
        """
        assert isinstance(content, str), content
        assert isinstance(encoding, str), encoding
        post_parameters = {
            "content": content,
            "encoding": encoding,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/blobs",
            input=post_parameters
        )
        return github.GitBlob.GitBlob(self._requester, headers, data, completed=True)

    def create_git_commit(self, message, tree, parents, author=github.GithubObject.NotSet, committer=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/git/commits <http://developer.github.com/v3/git/commits>`_
        :param message: string
        :param tree: :class:`github.GitTree.GitTree`
        :param parents: list of :class:`github.GitCommit.GitCommit`
        :param author: :class:`github.InputGitAuthor.InputGitAuthor`
        :param committer: :class:`github.InputGitAuthor.InputGitAuthor`
        :rtype: :class:`github.GitCommit.GitCommit`
        """
        assert isinstance(message, str), message
        assert isinstance(tree, github.GitTree.GitTree), tree
        assert all(isinstance(element, github.GitCommit.GitCommit) for element in parents), parents
        assert author is github.GithubObject.NotSet or isinstance(author, github.InputGitAuthor), author
        assert committer is github.GithubObject.NotSet or isinstance(committer, github.InputGitAuthor), committer
        post_parameters = {
            "message": message,
            "tree": tree._identity,
            "parents": [element._identity for element in parents],
        }
        if author is not github.GithubObject.NotSet:
            post_parameters["author"] = author._identity
        if committer is not github.GithubObject.NotSet:
            post_parameters["committer"] = committer._identity
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/commits",
            input=post_parameters
        )
        return github.GitCommit.GitCommit(self._requester, headers, data, completed=True)

    def create_git_ref(self, ref, sha):
        """
        :calls: `POST /repos/:owner/:repo/git/refs <http://developer.github.com/v3/git/refs>`_
        :param ref: string
        :param sha: string
        :rtype: :class:`github.GitRef.GitRef`
        """
        assert isinstance(ref, str), ref
        assert isinstance(sha, str), sha
        post_parameters = {
            "ref": ref,
            "sha": sha,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/refs",
            input=post_parameters
        )
        return github.GitRef.GitRef(self._requester, headers, data, completed=True)

    def create_git_tag(self, tag, message, object, type, tagger=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/git/tags <http://developer.github.com/v3/git/tags>`_
        :param tag: string
        :param message: string
        :param object: string
        :param type: string
        :param tagger: :class:`github.InputGitAuthor.InputGitAuthor`
        :rtype: :class:`github.GitTag.GitTag`
        """
        assert isinstance(tag, str), tag
        assert isinstance(message, str), message
        assert isinstance(object, str), object
        assert isinstance(type, str), type
        assert tagger is github.GithubObject.NotSet or isinstance(tagger, github.InputGitAuthor), tagger
        post_parameters = {
            "tag": tag,
            "message": message,
            "object": object,
            "type": type,
        }
        if tagger is not github.GithubObject.NotSet:
            post_parameters["tagger"] = tagger._identity
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/tags",
            input=post_parameters
        )
        return github.GitTag.GitTag(self._requester, headers, data, completed=True)

    def create_git_tree(self, tree, base_tree=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/git/trees <http://developer.github.com/v3/git/trees>`_
        :param tree: list of :class:`github.InputGitTreeElement.InputGitTreeElement`
        :param base_tree: :class:`github.GitTree.GitTree`
        :rtype: :class:`github.GitTree.GitTree`
        """
        assert all(isinstance(element, github.InputGitTreeElement) for element in tree), tree
        assert base_tree is github.GithubObject.NotSet or isinstance(base_tree, github.GitTree.GitTree), base_tree
        post_parameters = {
            "tree": [element._identity for element in tree],
        }
        if base_tree is not github.GithubObject.NotSet:
            post_parameters["base_tree"] = base_tree._identity
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/git/trees",
            input=post_parameters
        )
        return github.GitTree.GitTree(self._requester, headers, data, completed=True)

    def create_hook(self, name, config, events=github.GithubObject.NotSet, active=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/hooks <http://developer.github.com/v3/repos/hooks>`_
        :param name: string
        :param config: dict
        :param events: list of string
        :param active: bool
        :rtype: :class:`github.Hook.Hook`
        """
        assert isinstance(name, str), name
        assert isinstance(config, dict), config
        assert events is github.GithubObject.NotSet or all(isinstance(element, str) for element in events), events
        assert active is github.GithubObject.NotSet or isinstance(active, bool), active
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not github.GithubObject.NotSet:
            post_parameters["events"] = events
        if active is not github.GithubObject.NotSet:
            post_parameters["active"] = active
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/hooks",
            input=post_parameters
        )
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def create_issue(self, title, body=github.GithubObject.NotSet, assignee=github.GithubObject.NotSet, milestone=github.GithubObject.NotSet, labels=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/issues <http://developer.github.com/v3/issues>`_
        :param title: string
        :param body: string
        :param assignee: string or :class:`github.NamedUser.NamedUser`
        :param milestone: :class:`github.Milestone.Milestone`
        :param labels: list of :class:`github.Label.Label`
        :rtype: :class:`github.Issue.Issue`
        """
        assert isinstance(title, str), title
        assert body is github.GithubObject.NotSet or isinstance(body, str), body
        assert assignee is github.GithubObject.NotSet or isinstance(assignee, github.NamedUser.NamedUser) or isinstance(assignee, str), assignee
        assert milestone is github.GithubObject.NotSet or isinstance(milestone, github.Milestone.Milestone), milestone
        assert labels is github.GithubObject.NotSet or all(isinstance(element, github.Label.Label) for element in labels), labels
        post_parameters = {
            "title": title,
        }
        if body is not github.GithubObject.NotSet:
            post_parameters["body"] = body
        if assignee is not github.GithubObject.NotSet:
            if isinstance(assignee, str):
                post_parameters["assignee"] = assignee
            else:
                post_parameters["assignee"] = assignee._identity
        if milestone is not github.GithubObject.NotSet:
            post_parameters["milestone"] = milestone._identity
        if labels is not github.GithubObject.NotSet:
            post_parameters["labels"] = [element.name for element in labels]
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/issues",
            input=post_parameters
        )
        return github.Issue.Issue(self._requester, headers, data, completed=True)

    def create_key(self, title, key):
        """
        :calls: `POST /repos/:owner/:repo/keys <http://developer.github.com/v3/repos/keys>`_
        :param title: string
        :param key: string
        :rtype: :class:`github.RepositoryKey.RepositoryKey`
        """
        assert isinstance(title, str), title
        assert isinstance(key, str), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/keys",
            input=post_parameters
        )
        return github.RepositoryKey.RepositoryKey(self._requester, headers, data, completed=True, repoUrl=self.url)

    def create_label(self, name, color):
        """
        :calls: `POST /repos/:owner/:repo/labels <http://developer.github.com/v3/issues/labels>`_
        :param name: string
        :param color: string
        :rtype: :class:`github.Label.Label`
        """
        assert isinstance(name, str), name
        assert isinstance(color, str), color
        post_parameters = {
            "name": name,
            "color": color,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/labels",
            input=post_parameters
        )
        return github.Label.Label(self._requester, headers, data, completed=True)

    def create_milestone(self, title, state=github.GithubObject.NotSet, description=github.GithubObject.NotSet, due_on=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/milestones <http://developer.github.com/v3/issues/milestones>`_
        :param title: string
        :param state: string
        :param description: string
        :param due_on: date
        :rtype: :class:`github.Milestone.Milestone`
        """
        assert isinstance(title, str), title
        assert state is github.GithubObject.NotSet or isinstance(state, str), state
        assert description is github.GithubObject.NotSet or isinstance(description, str), description
        assert due_on is github.GithubObject.NotSet or isinstance(due_on, datetime.date), due_on
        post_parameters = {
            "title": title,
        }
        if state is not github.GithubObject.NotSet:
            post_parameters["state"] = state
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if due_on is not github.GithubObject.NotSet:
            post_parameters["due_on"] = due_on.strftime("%Y-%m-%d")
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/milestones",
            input=post_parameters
        )
        return github.Milestone.Milestone(self._requester, headers, data, completed=True)

    def create_pull(self, *args, **kwds):
        """
        :calls: `POST /repos/:owner/:repo/pulls <http://developer.github.com/v3/pulls>`_
        :param title: string
        :param body: string
        :param issue: :class:`github.Issue.Issue`
        :param base: string
        :param head: string
        :rtype: :class:`github.PullRequest.PullRequest`
        """
        if len(args) + len(kwds) == 4:
            return self.__create_pull_1(*args, **kwds)
        else:
            return self.__create_pull_2(*args, **kwds)

    def __create_pull_1(self, title, body, base, head):
        assert isinstance(title, str), title
        assert isinstance(body, str), body
        assert isinstance(base, str), base
        assert isinstance(head, str), head
        return self.__create_pull(title=title, body=body, base=base, head=head)

    def __create_pull_2(self, issue, base, head):
        assert isinstance(issue, github.Issue.Issue), issue
        assert isinstance(base, str), base
        assert isinstance(head, str), head
        return self.__create_pull(issue=issue._identity, base=base, head=head)

    def __create_pull(self, **kwds):
        post_parameters = kwds
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/pulls",
            input=post_parameters
        )
        return github.PullRequest.PullRequest(self._requester, headers, data, completed=True)

    def delete(self):
        """
        :calls: `DELETE /repos/:owner/:repo <http://developer.github.com/v3/repos>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url
        )

    def edit(self, name, description=github.GithubObject.NotSet, homepage=github.GithubObject.NotSet, private=github.GithubObject.NotSet, has_issues=github.GithubObject.NotSet, has_wiki=github.GithubObject.NotSet, has_downloads=github.GithubObject.NotSet, default_branch=github.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:owner/:repo <http://developer.github.com/v3/repos>`_
        :param name: string
        :param description: string
        :param homepage: string
        :param private: bool
        :param has_issues: bool
        :param has_wiki: bool
        :param has_downloads: bool
        :param default_branch: string
        :rtype: None
        """
        assert isinstance(name, str), name
        assert description is github.GithubObject.NotSet or isinstance(description, str), description
        assert homepage is github.GithubObject.NotSet or isinstance(homepage, str), homepage
        assert private is github.GithubObject.NotSet or isinstance(private, bool), private
        assert has_issues is github.GithubObject.NotSet or isinstance(has_issues, bool), has_issues
        assert has_wiki is github.GithubObject.NotSet or isinstance(has_wiki, bool), has_wiki
        assert has_downloads is github.GithubObject.NotSet or isinstance(has_downloads, bool), has_downloads
        assert default_branch is github.GithubObject.NotSet or isinstance(default_branch, str), default_branch
        post_parameters = {
            "name": name,
        }
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if homepage is not github.GithubObject.NotSet:
            post_parameters["homepage"] = homepage
        if private is not github.GithubObject.NotSet:
            post_parameters["private"] = private
        if has_issues is not github.GithubObject.NotSet:
            post_parameters["has_issues"] = has_issues
        if has_wiki is not github.GithubObject.NotSet:
            post_parameters["has_wiki"] = has_wiki
        if has_downloads is not github.GithubObject.NotSet:
            post_parameters["has_downloads"] = has_downloads
        if default_branch is not github.GithubObject.NotSet:
            post_parameters["default_branch"] = default_branch
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def get_archive_link(self, archive_format, ref=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/:archive_format/:ref <http://developer.github.com/v3/repos/contents>`_
        :param archive_format: string
        :param ref: string
        :rtype: string
        """
        assert isinstance(archive_format, str), archive_format
        assert ref is github.GithubObject.NotSet or isinstance(ref, str), ref
        url = self.url + "/" + archive_format
        if ref is not github.GithubObject.NotSet:
            url += "/" + ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            url
        )
        return headers["location"]

    def get_assignees(self):
        """
        :calls: `GET /repos/:owner/:repo/assignees <http://developer.github.com/v3/issues/assignees>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/assignees",
            None
        )

    def get_branch(self, branch):
        """
        :calls: `GET /repos/:owner/:repo/branches/:branch <http://developer.github.com/v3/repos>`_
        :param branch: string
        :rtype: :class:`github.Branch.Branch`
        """
        assert isinstance(branch, str), branch
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/branches/" + branch
        )
        return github.Branch.Branch(self._requester, headers, data, completed=True)

    def get_branches(self):
        """
        :calls: `GET /repos/:owner/:repo/branches <http://developer.github.com/v3/repos>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Branch.Branch`
        """
        return github.PaginatedList.PaginatedList(
            github.Branch.Branch,
            self._requester,
            self.url + "/branches",
            None
        )

    def get_collaborators(self):
        """
        :calls: `GET /repos/:owner/:repo/collaborators <http://developer.github.com/v3/repos/collaborators>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/collaborators",
            None
        )

    def get_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/comments/:id <http://developer.github.com/v3/repos/comments>`_
        :param id: integer
        :rtype: :class:`github.CommitComment.CommitComment`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/comments/" + str(id)
        )
        return github.CommitComment.CommitComment(self._requester, headers, data, completed=True)

    def get_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/comments <http://developer.github.com/v3/repos/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.CommitComment.CommitComment`
        """
        return github.PaginatedList.PaginatedList(
            github.CommitComment.CommitComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_commit(self, sha):
        """
        :calls: `GET /repos/:owner/:repo/commits/:sha <http://developer.github.com/v3/repos/commits>`_
        :param sha: string
        :rtype: :class:`github.Commit.Commit`
        """
        assert isinstance(sha, str), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/commits/" + sha
        )
        return github.Commit.Commit(self._requester, headers, data, completed=True)

    def get_commits(self, sha=github.GithubObject.NotSet, path=github.GithubObject.NotSet, since=github.GithubObject.NotSet, until=github.GithubObject.NotSet, author=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/commits <http://developer.github.com/v3/repos/commits>`_
        :param sha: string
        :param path: string
        :param since: datetime.datetime
        :param until: datetime.datetime
        :param author: string or :class:`github.NamedUser.NamedUser` or :class:`github.AuthenticatedUser.AuthenticatedUser`
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Commit.Commit`
        """
        assert sha is github.GithubObject.NotSet or isinstance(sha, str), sha
        assert path is github.GithubObject.NotSet or isinstance(path, str), path
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        assert until is github.GithubObject.NotSet or isinstance(until, datetime.datetime), until
        assert author is github.GithubObject.NotSet or isinstance(author, (str, github.NamedUser.NamedUser, github.AuthenticatedUser.AuthenticatedUser)), author
        url_parameters = dict()
        if sha is not github.GithubObject.NotSet:
            url_parameters["sha"] = sha
        if path is not github.GithubObject.NotSet:
            url_parameters["path"] = path
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        if until is not github.GithubObject.NotSet:
            url_parameters["until"] = until.strftime("%Y-%m-%dT%H:%M:%SZ")
        if author is not github.GithubObject.NotSet:
            if isinstance(author, (github.NamedUser.NamedUser, github.AuthenticatedUser.AuthenticatedUser)):
                url_parameters["author"] = author.login
            else:
                url_parameters["author"] = author
        return github.PaginatedList.PaginatedList(
            github.Commit.Commit,
            self._requester,
            self.url + "/commits",
            url_parameters
        )

    def get_contents(self, path, ref=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents>`_
        :param path: string
        :param ref: string
        :rtype: :class:`github.ContentFile.ContentFile`
        """
        return self.get_file_contents(path, ref)

    def get_file_contents(self, path, ref=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents>`_
        :param path: string
        :param ref: string
        :rtype: :class:`github.ContentFile.ContentFile`
        """
        assert isinstance(path, str), path
        assert ref is github.GithubObject.NotSet or isinstance(ref, str), ref
        url_parameters = dict()
        if ref is not github.GithubObject.NotSet:
            url_parameters["ref"] = ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/contents" + path,
            parameters=url_parameters
        )
        return github.ContentFile.ContentFile(self._requester, headers, data, completed=True)

    def get_dir_contents(self, path, ref=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents>`_
        :param path: string
        :param ref: string
        :rtype: list of :class:`github.ContentFile.ContentFile`
        """
        assert isinstance(path, str), path
        assert ref is github.GithubObject.NotSet or isinstance(ref, str), ref
        url_parameters = dict()
        if ref is not github.GithubObject.NotSet:
            url_parameters["ref"] = ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/contents" + path,
            parameters=url_parameters
        )

        # Handle 302 redirect response
        if headers.get('status') == '302 Found' and headers.get('location'):
            headers, data = self._requester.requestJsonAndCheck(
                "GET",
                headers['location'],
                parameters=url_parameters
            )

        return [
            github.ContentFile.ContentFile(self._requester, headers, attributes, completed=(attributes["type"] != "file"))  # Lazy completion only makes sense for files. See discussion here: https://github.com/jacquev6/PyGithub/issues/140#issuecomment-13481130
            for attributes in data
        ]

    def get_contributors(self):
        """
        :calls: `GET /repos/:owner/:repo/contributors <http://developer.github.com/v3/repos>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/contributors",
            None
        )

    def get_download(self, id):
        """
        :calls: `GET /repos/:owner/:repo/downloads/:id <http://developer.github.com/v3/repos/downloads>`_
        :param id: integer
        :rtype: :class:`github.Download.Download`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/downloads/" + str(id)
        )
        return github.Download.Download(self._requester, headers, data, completed=True)

    def get_downloads(self):
        """
        :calls: `GET /repos/:owner/:repo/downloads <http://developer.github.com/v3/repos/downloads>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Download.Download`
        """
        return github.PaginatedList.PaginatedList(
            github.Download.Download,
            self._requester,
            self.url + "/downloads",
            None
        )

    def get_events(self):
        """
        :calls: `GET /repos/:owner/:repo/events <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            self.url + "/events",
            None
        )

    def get_forks(self):
        """
        :calls: `GET /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            Repository,
            self._requester,
            self.url + "/forks",
            None
        )

    def get_git_blob(self, sha):
        """
        :calls: `GET /repos/:owner/:repo/git/blobs/:sha <http://developer.github.com/v3/git/blobs>`_
        :param sha: string
        :rtype: :class:`github.GitBlob.GitBlob`
        """
        assert isinstance(sha, str), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/blobs/" + sha
        )
        return github.GitBlob.GitBlob(self._requester, headers, data, completed=True)

    def get_git_commit(self, sha):
        """
        :calls: `GET /repos/:owner/:repo/git/commits/:sha <http://developer.github.com/v3/git/commits>`_
        :param sha: string
        :rtype: :class:`github.GitCommit.GitCommit`
        """
        assert isinstance(sha, str), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/commits/" + sha
        )
        return github.GitCommit.GitCommit(self._requester, headers, data, completed=True)

    def get_git_ref(self, ref):
        """
        :calls: `GET /repos/:owner/:repo/git/refs/:ref <http://developer.github.com/v3/git/refs>`_
        :param ref: string
        :rtype: :class:`github.GitRef.GitRef`
        """
        prefix = "/git/refs/"
        if not self._requester.FIX_REPO_GET_GIT_REF:
            prefix = "/git/"
        assert isinstance(ref, str), ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + prefix + ref
        )
        return github.GitRef.GitRef(self._requester, headers, data, completed=True)

    def get_git_refs(self):
        """
        :calls: `GET /repos/:owner/:repo/git/refs <http://developer.github.com/v3/git/refs>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.GitRef.GitRef`
        """
        return github.PaginatedList.PaginatedList(
            github.GitRef.GitRef,
            self._requester,
            self.url + "/git/refs",
            None
        )

    def get_git_tag(self, sha):
        """
        :calls: `GET /repos/:owner/:repo/git/tags/:sha <http://developer.github.com/v3/git/tags>`_
        :param sha: string
        :rtype: :class:`github.GitTag.GitTag`
        """
        assert isinstance(sha, str), sha
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/tags/" + sha
        )
        return github.GitTag.GitTag(self._requester, headers, data, completed=True)

    def get_git_tree(self, sha, recursive=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/git/trees/:sha <http://developer.github.com/v3/git/trees>`_
        :param sha: string
        :param recursive: bool
        :rtype: :class:`github.GitTree.GitTree`
        """
        assert isinstance(sha, str), sha
        assert recursive is github.GithubObject.NotSet or isinstance(recursive, bool), recursive
        url_parameters = dict()
        if recursive is not github.GithubObject.NotSet:
            url_parameters["recursive"] = recursive
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/git/trees/" + sha,
            parameters=url_parameters
        )
        return github.GitTree.GitTree(self._requester, headers, data, completed=True)

    def get_hook(self, id):
        """
        :calls: `GET /repos/:owner/:repo/hooks/:id <http://developer.github.com/v3/repos/hooks>`_
        :param id: integer
        :rtype: :class:`github.Hook.Hook`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/hooks/" + str(id)
        )
        return github.Hook.Hook(self._requester, headers, data, completed=True)

    def get_hooks(self):
        """
        :calls: `GET /repos/:owner/:repo/hooks <http://developer.github.com/v3/repos/hooks>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Hook.Hook`
        """
        return github.PaginatedList.PaginatedList(
            github.Hook.Hook,
            self._requester,
            self.url + "/hooks",
            None
        )

    def get_issue(self, number):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number <http://developer.github.com/v3/issues>`_
        :param number: integer
        :rtype: :class:`github.Issue.Issue`
        """
        assert isinstance(number, int), number
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/issues/" + str(number)
        )
        return github.Issue.Issue(self._requester, headers, data, completed=True)

    def get_issues(self, milestone=github.GithubObject.NotSet, state=github.GithubObject.NotSet, assignee=github.GithubObject.NotSet, mentioned=github.GithubObject.NotSet, labels=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/issues <http://developer.github.com/v3/issues>`_
        :param milestone: :class:`github.Milestone.Milestone` or "none" or "*"
        :param state: string
        :param assignee: string or :class:`github.NamedUser.NamedUser` or "none" or "*"
        :param mentioned: :class:`github.NamedUser.NamedUser`
        :param labels: list of :class:`github.Label.Label`
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert milestone is github.GithubObject.NotSet or milestone == "*" or milestone == "none" or isinstance(milestone, github.Milestone.Milestone), milestone
        assert state is github.GithubObject.NotSet or isinstance(state, str), state
        assert assignee is github.GithubObject.NotSet or isinstance(assignee, github.NamedUser.NamedUser) or isinstance(assignee, str), assignee
        assert mentioned is github.GithubObject.NotSet or isinstance(mentioned, github.NamedUser.NamedUser), mentioned
        assert labels is github.GithubObject.NotSet or all(isinstance(element, github.Label.Label) for element in labels), labels
        assert sort is github.GithubObject.NotSet or isinstance(sort, str), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, str), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if milestone is not github.GithubObject.NotSet:
            if isinstance(milestone, str):
                url_parameters["milestone"] = milestone
            else:
                url_parameters["milestone"] = milestone._identity
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        if assignee is not github.GithubObject.NotSet:
            if isinstance(assignee, str):
                url_parameters["assignee"] = assignee
            else:
                url_parameters["assignee"] = assignee._identity
        if mentioned is not github.GithubObject.NotSet:
            url_parameters["mentioned"] = mentioned._identity
        if labels is not github.GithubObject.NotSet:
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.Issue.Issue,
            self._requester,
            self.url + "/issues",
            url_parameters
        )

    def get_issues_comments(self, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/issues/comments <http://developer.github.com/v3/issues/comments>`_
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueComment.IssueComment`
        """
        assert sort is github.GithubObject.NotSet or isinstance(sort, str), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, str), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            self.url + "/issues/comments",
            url_parameters
        )

    def get_issues_event(self, id):
        """
        :calls: `GET /repos/:owner/:repo/issues/events/:id <http://developer.github.com/v3/issues/events>`_
        :param id: integer
        :rtype: :class:`github.IssueEvent.IssueEvent`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/issues/events/" + str(id)
        )
        return github.IssueEvent.IssueEvent(self._requester, headers, data, completed=True)

    def get_issues_events(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/events <http://developer.github.com/v3/issues/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueEvent.IssueEvent`
        """
        return github.PaginatedList.PaginatedList(
            github.IssueEvent.IssueEvent,
            self._requester,
            self.url + "/issues/events",
            None
        )

    def get_key(self, id):
        """
        :calls: `GET /repos/:owner/:repo/keys/:id <http://developer.github.com/v3/repos/keys>`_
        :param id: integer
        :rtype: :class:`github.RepositoryKey.RepositoryKey`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/keys/" + str(id)
        )
        return github.RepositoryKey.RepositoryKey(self._requester, headers, data, completed=True, repoUrl=self.url)

    def get_keys(self):
        """
        :calls: `GET /repos/:owner/:repo/keys <http://developer.github.com/v3/repos/keys>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.RepositoryKey.RepositoryKey`
        """
        return github.PaginatedList.PaginatedList(
            lambda requester, headers, data, completed: github.RepositoryKey.RepositoryKey(requester, headers, data, completed, repoUrl=self.url),
            self._requester,
            self.url + "/keys",
            None
        )

    def get_label(self, name):
        """
        :calls: `GET /repos/:owner/:repo/labels/:name <http://developer.github.com/v3/issues/labels>`_
        :param name: string
        :rtype: :class:`github.Label.Label`
        """
        assert isinstance(name, str), name
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/labels/" + urllib.parse.quote(name)
        )
        return github.Label.Label(self._requester, headers, data, completed=True)

    def get_labels(self):
        """
        :calls: `GET /repos/:owner/:repo/labels <http://developer.github.com/v3/issues/labels>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Label.Label`
        """
        return github.PaginatedList.PaginatedList(
            github.Label.Label,
            self._requester,
            self.url + "/labels",
            None
        )

    def get_languages(self):
        """
        :calls: `GET /repos/:owner/:repo/languages <http://developer.github.com/v3/repos>`_
        :rtype: dict of string to integer
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/languages"
        )
        return data

    def get_milestone(self, number):
        """
        :calls: `GET /repos/:owner/:repo/milestones/:number <http://developer.github.com/v3/issues/milestones>`_
        :param number: integer
        :rtype: :class:`github.Milestone.Milestone`
        """
        assert isinstance(number, int), number
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/milestones/" + str(number)
        )
        return github.Milestone.Milestone(self._requester, headers, data, completed=True)

    def get_milestones(self, state=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/milestones <http://developer.github.com/v3/issues/milestones>`_
        :param state: string
        :param sort: string
        :param direction: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Milestone.Milestone`
        """
        assert state is github.GithubObject.NotSet or isinstance(state, str), state
        assert sort is github.GithubObject.NotSet or isinstance(sort, str), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, str), direction
        url_parameters = dict()
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        return github.PaginatedList.PaginatedList(
            github.Milestone.Milestone,
            self._requester,
            self.url + "/milestones",
            url_parameters
        )

    def get_network_events(self):
        """
        :calls: `GET /networks/:owner/:repo/events <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            "/networks/" + self.owner.login + "/" + self.name + "/events",
            None
        )

    def get_pull(self, number):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number <http://developer.github.com/v3/pulls>`_
        :param number: integer
        :rtype: :class:`github.PullRequest.PullRequest`
        """
        assert isinstance(number, int), number
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/pulls/" + str(number)
        )
        return github.PullRequest.PullRequest(self._requester, headers, data, completed=True)

    def get_pulls(self, state=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/pulls <http://developer.github.com/v3/pulls>`_
        :param state: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequest.PullRequest`
        """
        assert state is github.GithubObject.NotSet or isinstance(state, str), state
        url_parameters = dict()
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        return github.PaginatedList.PaginatedList(
            github.PullRequest.PullRequest,
            self._requester,
            self.url + "/pulls",
            url_parameters
        )

    def get_pulls_comments(self, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/pulls/comments <http://developer.github.com/v3/pulls/comments>`_
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        return self.get_pulls_review_comments(sort, direction, since)

    def get_pulls_review_comments(self, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/pulls/comments <http://developer.github.com/v3/pulls/comments>`_
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        assert sort is github.GithubObject.NotSet or isinstance(sort, str), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, str), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            self.url + "/pulls/comments",
            url_parameters
        )

    def get_readme(self, ref=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/readme <http://developer.github.com/v3/repos/contents>`_
        :param ref: string
        :rtype: :class:`github.ContentFile.ContentFile`
        """
        assert ref is github.GithubObject.NotSet or isinstance(ref, str), ref
        url_parameters = dict()
        if ref is not github.GithubObject.NotSet:
            url_parameters["ref"] = ref
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/readme",
            parameters=url_parameters
        )
        return github.ContentFile.ContentFile(self._requester, headers, data, completed=True)

    def get_stargazers(self):
        """
        :calls: `GET /repos/:owner/:repo/stargazers <http://developer.github.com/v3/activity/starring>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/stargazers",
            None
        )

    def get_stats_contributors(self):
        """
        :calls: `GET /repos/:owner/:repo/stats/contributors <http://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts>`_
        :rtype: None or list of :class:`github.StatsContributor.StatsContributor`
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/stats/contributors"
        )
        if data == {}:
            return None
        else:
            return [
                github.StatsContributor.StatsContributor(self._requester, headers, attributes, completed=True)
                for attributes in data
            ]

    def get_stats_commit_activity(self):
        """
        :calls: `GET /repos/:owner/:repo/stats/commit_activity <developer.github.com/v3/repos/statistics/#get-the-number-of-commits-per-hour-in-each-day>`_
        :rtype: None or list of :class:`github.StatsCommitActivity.StatsCommitActivity`
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/stats/commit_activity"
        )
        if data == {}:
            return None
        else:
            return [
                github.StatsCommitActivity.StatsCommitActivity(self._requester, headers, attributes, completed=True)
                for attributes in data
            ]

    def get_stats_code_frequency(self):
        """
        :calls: `GET /repos/:owner/:repo/stats/code_frequency <http://developer.github.com/v3/repos/statistics/#get-the-number-of-additions-and-deletions-per-week>`_
        :rtype: None or list of :class:`github.StatsCodeFrequency.StatsCodeFrequency`
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/stats/code_frequency"
        )
        if data == {}:
            return None
        else:
            return [
                github.StatsCodeFrequency.StatsCodeFrequency(self._requester, headers, attributes, completed=True)
                for attributes in data
            ]

    def get_stats_participation(self):
        """
        :calls: `GET /repos/:owner/:repo/stats/participation <http://developer.github.com/v3/repos/statistics/#get-the-weekly-commit-count-for-the-repo-owner-and-everyone-else>`_
        :rtype: None or :class:`github.StatsParticipation.StatsParticipation`
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/stats/participation"
        )
        if data == {}:
            return None
        else:
            return github.StatsParticipation.StatsParticipation(self._requester, headers, data, completed=True)

    def get_stats_punch_card(self):
        """
        :calls: `GET /repos/:owner/:repo/stats/punch_card <http://developer.github.com/v3/repos/statistics/#get-the-number-of-commits-per-hour-in-each-day>`_
        :rtype: None or :class:`github.StatsPunchCard.StatsPunchCard`
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.url + "/stats/punch_card"
        )
        if data == {}:
            return None
        else:
            return github.StatsPunchCard.StatsPunchCard(self._requester, headers, data, completed=True)

    def get_subscribers(self):
        """
        :calls: `GET /repos/:owner/:repo/subscribers <http://developer.github.com/v3/activity/watching>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/subscribers",
            None
        )

    def get_tags(self):
        """
        :calls: `GET /repos/:owner/:repo/tags <http://developer.github.com/v3/repos>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Tag.Tag`
        """
        return github.PaginatedList.PaginatedList(
            github.Tag.Tag,
            self._requester,
            self.url + "/tags",
            None
        )

    def get_teams(self):
        """
        :calls: `GET /repos/:owner/:repo/teams <http://developer.github.com/v3/repos>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Team.Team`
        """
        return github.PaginatedList.PaginatedList(
            github.Team.Team,
            self._requester,
            self.url + "/teams",
            None
        )

    def get_watchers(self):
        """
        :calls: `GET /repos/:owner/:repo/watchers <http://developer.github.com/v3/activity/starring>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/watchers",
            None
        )

    def has_in_assignees(self, assignee):
        """
        :calls: `GET /repos/:owner/:repo/assignees/:assignee <http://developer.github.com/v3/issues/assignees>`_
        :param assignee: string or :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(assignee, github.NamedUser.NamedUser) or isinstance(assignee, str), assignee

        if isinstance(assignee, github.NamedUser.NamedUser):
            assignee = assignee._identity

        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/assignees/" + assignee
        )
        return status == 204

    def has_in_collaborators(self, collaborator):
        """
        :calls: `GET /repos/:owner/:repo/collaborators/:user <http://developer.github.com/v3/repos/collaborators>`_
        :param collaborator: string or :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser) or isinstance(collaborator, str), collaborator

        if isinstance(collaborator, github.NamedUser.NamedUser):
            collaborator = collaborator._identity

        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/collaborators/" + collaborator
        )
        return status == 204

    def legacy_search_issues(self, state, keyword):
        """
        :calls: `GET /legacy/issues/search/:owner/:repository/:state/:keyword <http://developer.github.com/v3/search/legacy>`_
        :param state: "open" or "closed"
        :param keyword: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert state in ["open", "closed"], state
        assert isinstance(keyword, str), keyword
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/legacy/issues/search/" + self.owner.login + "/" + self.name + "/" + state + "/" + urllib.parse.quote(keyword)
        )
        return [
            github.Issue.Issue(self._requester, headers, github.Legacy.convertIssue(element), completed=False)
            for element in data["issues"]
        ]

    def merge(self, base, head, commit_message=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/merges <http://developer.github.com/v3/repos/merging>`_
        :param base: string
        :param head: string
        :param commit_message: string
        :rtype: :class:`github.Commit.Commit`
        """
        assert isinstance(base, str), base
        assert isinstance(head, str), head
        assert commit_message is github.GithubObject.NotSet or isinstance(commit_message, str), commit_message
        post_parameters = {
            "base": base,
            "head": head,
        }
        if commit_message is not github.GithubObject.NotSet:
            post_parameters["commit_message"] = commit_message
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/merges",
            input=post_parameters
        )
        if data is None:
            return None
        else:
            return github.Commit.Commit(self._requester, headers, data, completed=True)

    def remove_from_collaborators(self, collaborator):
        """
        :calls: `DELETE /repos/:owner/:repo/collaborators/:user <http://developer.github.com/v3/repos/collaborators>`_
        :param collaborator: string or :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(collaborator, github.NamedUser.NamedUser) or isinstance(collaborator, str), collaborator

        if isinstance(collaborator, github.NamedUser.NamedUser):
            collaborator = collaborator._identity

        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/collaborators/" + collaborator
        )

    def subscribe_to_hub(self, event, callback, secret=github.GithubObject.NotSet):
        """
        :calls: `POST /hub <http://developer.github.com/>`_
        :param event: string
        :param callback: string
        :param secret: string
        :rtype: None
        """
        return self._hub("subscribe", event, callback, secret)

    def unsubscribe_from_hub(self, event, callback):
        """
        :calls: `POST /hub <http://developer.github.com/>`_
        :param event: string
        :param callback: string
        :param secret: string
        :rtype: None
        """
        return self._hub("unsubscribe", event, callback, github.GithubObject.NotSet)

    def _hub(self, mode, event, callback, secret):
        assert isinstance(mode, str), mode
        assert isinstance(event, str), event
        assert isinstance(callback, str), callback
        assert secret is github.GithubObject.NotSet or isinstance(secret, str), secret

        post_parameters = {
            "hub.mode": mode,
            "hub.topic": "https://github.com/" + self.full_name + "/events/" + event,
            "hub.callback": callback,
        }
        if secret is not github.GithubObject.NotSet:
            post_parameters["hub.secret"] = secret

        headers, output = self._requester.requestMultipartAndCheck(
            "POST",
            "/hub",
            input=post_parameters
        )

    @property
    def _identity(self):
        return self.owner.login + "/" + self.name

    def _initAttributes(self):
        self._archive_url = github.GithubObject.NotSet
        self._assignees_url = github.GithubObject.NotSet
        self._blobs_url = github.GithubObject.NotSet
        self._branches_url = github.GithubObject.NotSet
        self._clone_url = github.GithubObject.NotSet
        self._collaborators_url = github.GithubObject.NotSet
        self._comments_url = github.GithubObject.NotSet
        self._commits_url = github.GithubObject.NotSet
        self._compare_url = github.GithubObject.NotSet
        self._contents_url = github.GithubObject.NotSet
        self._contributors_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._default_branch = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._downloads_url = github.GithubObject.NotSet
        self._events_url = github.GithubObject.NotSet
        self._fork = github.GithubObject.NotSet
        self._forks = github.GithubObject.NotSet
        self._forks_count = github.GithubObject.NotSet
        self._forks_url = github.GithubObject.NotSet
        self._full_name = github.GithubObject.NotSet
        self._git_commits_url = github.GithubObject.NotSet
        self._git_refs_url = github.GithubObject.NotSet
        self._git_tags_url = github.GithubObject.NotSet
        self._git_url = github.GithubObject.NotSet
        self._has_downloads = github.GithubObject.NotSet
        self._has_issues = github.GithubObject.NotSet
        self._has_wiki = github.GithubObject.NotSet
        self._homepage = github.GithubObject.NotSet
        self._hooks_url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._issue_comment_url = github.GithubObject.NotSet
        self._issue_events_url = github.GithubObject.NotSet
        self._issues_url = github.GithubObject.NotSet
        self._keys_url = github.GithubObject.NotSet
        self._labels_url = github.GithubObject.NotSet
        self._language = github.GithubObject.NotSet
        self._languages_url = github.GithubObject.NotSet
        self._master_branch = github.GithubObject.NotSet
        self._merges_url = github.GithubObject.NotSet
        self._milestones_url = github.GithubObject.NotSet
        self._mirror_url = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._network_count = github.GithubObject.NotSet
        self._notifications_url = github.GithubObject.NotSet
        self._open_issues = github.GithubObject.NotSet
        self._open_issues_count = github.GithubObject.NotSet
        self._organization = github.GithubObject.NotSet
        self._owner = github.GithubObject.NotSet
        self._parent = github.GithubObject.NotSet
        self._permissions = github.GithubObject.NotSet
        self._private = github.GithubObject.NotSet
        self._pulls_url = github.GithubObject.NotSet
        self._pushed_at = github.GithubObject.NotSet
        self._size = github.GithubObject.NotSet
        self._source = github.GithubObject.NotSet
        self._ssh_url = github.GithubObject.NotSet
        self._stargazers_count = github.GithubObject.NotSet
        self._stargazers_url = github.GithubObject.NotSet
        self._statuses_url = github.GithubObject.NotSet
        self._subscribers_url = github.GithubObject.NotSet
        self._subscription_url = github.GithubObject.NotSet
        self._svn_url = github.GithubObject.NotSet
        self._tags_url = github.GithubObject.NotSet
        self._teams_url = github.GithubObject.NotSet
        self._trees_url = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._watchers = github.GithubObject.NotSet
        self._watchers_count = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "archive_url" in attributes:  # pragma no branch
            self._archive_url = self._makeStringAttribute(attributes["archive_url"])
        if "assignees_url" in attributes:  # pragma no branch
            self._assignees_url = self._makeStringAttribute(attributes["assignees_url"])
        if "blobs_url" in attributes:  # pragma no branch
            self._blobs_url = self._makeStringAttribute(attributes["blobs_url"])
        if "branches_url" in attributes:  # pragma no branch
            self._branches_url = self._makeStringAttribute(attributes["branches_url"])
        if "clone_url" in attributes:  # pragma no branch
            self._clone_url = self._makeStringAttribute(attributes["clone_url"])
        if "collaborators_url" in attributes:  # pragma no branch
            self._collaborators_url = self._makeStringAttribute(attributes["collaborators_url"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commits_url" in attributes:  # pragma no branch
            self._commits_url = self._makeStringAttribute(attributes["commits_url"])
        if "compare_url" in attributes:  # pragma no branch
            self._compare_url = self._makeStringAttribute(attributes["compare_url"])
        if "contents_url" in attributes:  # pragma no branch
            self._contents_url = self._makeStringAttribute(attributes["contents_url"])
        if "contributors_url" in attributes:  # pragma no branch
            self._contributors_url = self._makeStringAttribute(attributes["contributors_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "default_branch" in attributes:  # pragma no branch
            self._default_branch = self._makeStringAttribute(attributes["default_branch"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "downloads_url" in attributes:  # pragma no branch
            self._downloads_url = self._makeStringAttribute(attributes["downloads_url"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "fork" in attributes:  # pragma no branch
            self._fork = self._makeBoolAttribute(attributes["fork"])
        if "forks" in attributes:  # pragma no branch
            self._forks = self._makeIntAttribute(attributes["forks"])
        if "forks_count" in attributes:  # pragma no branch
            self._forks_count = self._makeIntAttribute(attributes["forks_count"])
        if "forks_url" in attributes:  # pragma no branch
            self._forks_url = self._makeStringAttribute(attributes["forks_url"])
        if "full_name" in attributes:  # pragma no branch
            self._full_name = self._makeStringAttribute(attributes["full_name"])
        if "git_commits_url" in attributes:  # pragma no branch
            self._git_commits_url = self._makeStringAttribute(attributes["git_commits_url"])
        if "git_refs_url" in attributes:  # pragma no branch
            self._git_refs_url = self._makeStringAttribute(attributes["git_refs_url"])
        if "git_tags_url" in attributes:  # pragma no branch
            self._git_tags_url = self._makeStringAttribute(attributes["git_tags_url"])
        if "git_url" in attributes:  # pragma no branch
            self._git_url = self._makeStringAttribute(attributes["git_url"])
        if "has_downloads" in attributes:  # pragma no branch
            self._has_downloads = self._makeBoolAttribute(attributes["has_downloads"])
        if "has_issues" in attributes:  # pragma no branch
            self._has_issues = self._makeBoolAttribute(attributes["has_issues"])
        if "has_wiki" in attributes:  # pragma no branch
            self._has_wiki = self._makeBoolAttribute(attributes["has_wiki"])
        if "homepage" in attributes:  # pragma no branch
            self._homepage = self._makeStringAttribute(attributes["homepage"])
        if "hooks_url" in attributes:  # pragma no branch
            self._hooks_url = self._makeStringAttribute(attributes["hooks_url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "issue_comment_url" in attributes:  # pragma no branch
            self._issue_comment_url = self._makeStringAttribute(attributes["issue_comment_url"])
        if "issue_events_url" in attributes:  # pragma no branch
            self._issue_events_url = self._makeStringAttribute(attributes["issue_events_url"])
        if "issues_url" in attributes:  # pragma no branch
            self._issues_url = self._makeStringAttribute(attributes["issues_url"])
        if "keys_url" in attributes:  # pragma no branch
            self._keys_url = self._makeStringAttribute(attributes["keys_url"])
        if "labels_url" in attributes:  # pragma no branch
            self._labels_url = self._makeStringAttribute(attributes["labels_url"])
        if "language" in attributes:  # pragma no branch
            self._language = self._makeStringAttribute(attributes["language"])
        if "languages_url" in attributes:  # pragma no branch
            self._languages_url = self._makeStringAttribute(attributes["languages_url"])
        if "master_branch" in attributes:  # pragma no branch
            self._master_branch = self._makeStringAttribute(attributes["master_branch"])
        if "merges_url" in attributes:  # pragma no branch
            self._merges_url = self._makeStringAttribute(attributes["merges_url"])
        if "milestones_url" in attributes:  # pragma no branch
            self._milestones_url = self._makeStringAttribute(attributes["milestones_url"])
        if "mirror_url" in attributes:  # pragma no branch
            self._mirror_url = self._makeStringAttribute(attributes["mirror_url"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "network_count" in attributes:  # pragma no branch
            self._network_count = self._makeIntAttribute(attributes["network_count"])
        if "notifications_url" in attributes:  # pragma no branch
            self._notifications_url = self._makeStringAttribute(attributes["notifications_url"])
        if "open_issues" in attributes:  # pragma no branch
            self._open_issues = self._makeIntAttribute(attributes["open_issues"])
        if "open_issues_count" in attributes:  # pragma no branch
            self._open_issues_count = self._makeIntAttribute(attributes["open_issues_count"])
        if "organization" in attributes:  # pragma no branch
            self._organization = self._makeClassAttribute(github.Organization.Organization, attributes["organization"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["owner"])
        if "parent" in attributes:  # pragma no branch
            self._parent = self._makeClassAttribute(Repository, attributes["parent"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeClassAttribute(github.Permissions.Permissions, attributes["permissions"])
        if "private" in attributes:  # pragma no branch
            self._private = self._makeBoolAttribute(attributes["private"])
        if "pulls_url" in attributes:  # pragma no branch
            self._pulls_url = self._makeStringAttribute(attributes["pulls_url"])
        if "pushed_at" in attributes:  # pragma no branch
            self._pushed_at = self._makeDatetimeAttribute(attributes["pushed_at"])
        if "size" in attributes:  # pragma no branch
            self._size = self._makeIntAttribute(attributes["size"])
        if "source" in attributes:  # pragma no branch
            self._source = self._makeClassAttribute(Repository, attributes["source"])
        if "ssh_url" in attributes:  # pragma no branch
            self._ssh_url = self._makeStringAttribute(attributes["ssh_url"])
        if "stargazers_count" in attributes:  # pragma no branch
            self._stargazers_count = self._makeIntAttribute(attributes["stargazers_count"])
        if "stargazers_url" in attributes:  # pragma no branch
            self._stargazers_url = self._makeStringAttribute(attributes["stargazers_url"])
        if "statuses_url" in attributes:  # pragma no branch
            self._statuses_url = self._makeStringAttribute(attributes["statuses_url"])
        if "subscribers_url" in attributes:  # pragma no branch
            self._subscribers_url = self._makeStringAttribute(attributes["subscribers_url"])
        if "subscription_url" in attributes:  # pragma no branch
            self._subscription_url = self._makeStringAttribute(attributes["subscription_url"])
        if "svn_url" in attributes:  # pragma no branch
            self._svn_url = self._makeStringAttribute(attributes["svn_url"])
        if "tags_url" in attributes:  # pragma no branch
            self._tags_url = self._makeStringAttribute(attributes["tags_url"])
        if "teams_url" in attributes:  # pragma no branch
            self._teams_url = self._makeStringAttribute(attributes["teams_url"])
        if "trees_url" in attributes:  # pragma no branch
            self._trees_url = self._makeStringAttribute(attributes["trees_url"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "watchers" in attributes:  # pragma no branch
            self._watchers = self._makeIntAttribute(attributes["watchers"])
        if "watchers_count" in attributes:  # pragma no branch
            self._watchers_count = self._makeIntAttribute(attributes["watchers_count"])